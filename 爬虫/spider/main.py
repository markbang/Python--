import requests
from lxml import html
import re
import time
from my_fake_useragent import UserAgent
import random

urls = []
fault_urls = []
n = 0
with open(r'.\spider\class_urls.txt', 'r', encoding='utf-8') as f:
    for i in f.readlines():
        urls.append(i.strip())
headers = {
    "cookie": "_lxsdk_cuid=18c0a246cbfc8-0f5cdee6b7df49-4c657b58-1bcab9-18c0a246cbfc8; _lxsdk=18c0a246cbfc8-0f5cdee6b7df49-4c657b58-1bcab9-18c0a246cbfc8; _hc.v=46e4e47a-d572-9f84-324b-7e02d34b2cc6.1700977209; WEBDFPID=6x83uuxx28y751531z48y964z201wwy581x9z753v1597958u68uz6x9-2016337209566-1700977208649GACUUQGfd79fef3d01d5e9aadc18ccd4d0c95072717; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1700977352; fspop=test; cy=1; cye=shanghai; s_ViewType=10; _lx_utm=utm_source%3Dbing%26utm_medium%3Dorganic; ctu=db5a043e83de3903cae56b82830561fdbcf4e1462550d54b52104e68567c86c1; qruuid=17cd1a93-5b18-4471-9904-7ff375083242; dplet=7e06a93f5d7e81739a53c10fbfcfd101; dper=c6068d65c64d89efcedf0300fae2217ba51174ba0bd9e30ceae478d4aaf45f0cf8d25eb58de0bd58452e453eaacecce91003ad57e67e10627cb6908b5acf5585; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_4399452783; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1700980354; _lxsdk_s=18c0a4ca664-4d5-592-46f%7C%7C97",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Referer": "https",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": UserAgent().random(),
    "sec-ch-ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
# 地区分类的大众点评代号
address_list = {
    '静安区': 'r3',
    '长宁区': 'r4',
    '徐汇区': 'r2',
    '杨浦区': 'r10',
    '黄浦区': 'r6',
    '虹口区': 'r9',
    '普陀区': 'r7',
    '闵行区': 'r12',
    '宝山区': 'r13',
    '浦东新区': 'r5',
    '松江区': 'r5937',
    '嘉定区': 'r5938',
    '青浦区': 'r5939',
    '金山区': 'r8847',
    '奉贤区': 'r8846',
    '崇明区': 'c3580'
}
obj = re.compile(r'class="PageLink".*?">(?P<last_page>.*?)</a>.*?<a href=.*?title="下一页">下一页</a>',re.S)
for url in urls:
    base_url = url
    for address, code in address_list.items():
        url = base_url + code
        response = requests.get(url=url, headers=headers)
        match = obj.search(response.text)
        if match:
            last_page = match.group('last_page')
            for page_num in range(1, int(last_page) + 1):
                l_url = url + 'p' + str(page_num)
                print(l_url)
                headers.update({'Referer': l_url})
                response = requests.get(url=l_url, headers=headers)
                if response.status_code != 200:
                    fault_urls.append(l_url)
                    continue
                # 使用lxml解析HTML
                tree = html.fromstring(response.text)
                # 使用XPath选择所有在//*[@id="shop-all-list"]/ul下的li标签
                li_elements = tree.xpath('//*[@id="shop-all-list"]/ul/li')
                # 遍历每个li标签并提取数据
                for li_element in li_elements:
                    try:
                        # 提取商家名称
                        shop_name = li_element.xpath('.//div[@class="txt"]/div[@class="tit"]/a/h4/text()')[0]
                        # 提取商家URL
                        shop_url = li_element.xpath('.//div[@class="txt"]/div[@class="tit"]/a/@href')[0]
                        # 提取评价人数
                        review_count = li_element.xpath('.//div[@class="comment"]/a/b/text()')[0] if li_element.xpath('.//div[@class="comment"]/a/text()') != '我要评价' else 0
                        # 提取人均消费
                        avg_price = li_element.xpath('.//div[@class="comment"]/a[@class="mean-price"]/b/text()')[0].strip()
                        # 提取标签和地区
                        tags = li_element.xpath('.//div[@class="tag-addr"]/a/span[@class="tag"]/text()')[0]
                        regions = li_element.xpath('.//div[@class="tag-addr"]/a/span[@class="tag"]/text()')[1]
                        # 星级
                        stars = li_element.xpath('.//span[contains(@class, "star")]/@class')[0]
                        star = int(stars.split('_')[1].split(' ')[0]) / 10
                        #根据shopurl获取经纬度
                        shop_id = shop_url.split('/')[-1]
                        shop_g = requests.get('https://www.dianping.com/ajax/json/shopDynamic/shopAside?shopId='+shop_id, headers=headers)
                        shop_lng = shop_g.json()['shop']['glng']
                        shop_lat = shop_g.json()['shop']['glat']
                        # 口味，服务，环境
                        score_sourse = requests.get(f'https://www.dianping.com/ajax/json/shopDynamic/reviewAndStar?shopId={shop_id}&cityId=1&mainCategoryId=101')
                        score_list = score_sourse.json()['shopRefinedScoreValueList']
                        taste_score = score_list[0]
                        environment_score = score_list[1]
                        service_score = score_list[2]
                        business = requests.get(f'https://www.dianping.com/shop/{shop_id}')
                        if business.status_code == 403:
                            fault_urls.append(f'https://www.dianping.com/shop/{shop_id}')
                            continue
                        business_hours = business.text().split('营业时间：')[1].split('</p>')[0]
                        # 打印或保存数据
                        print('id', shop_id)
                        print("店名", shop_name)
                        print("分类", shop_url)
                        print("评价人数:", review_count)
                        print("价格", avg_price)
                        print('口味', taste_score)
                        print('服务', service_score)
                        print('环境', environment_score)
                        print('星级', star)
                        print("分类", tags)
                        print("reg", regions)
                        print('lng', shop_lng)
                        print('lat', shop_lat)
                        print('area', address)
                        print('营业时间', business_hours)
                        print("------------------")
                        time.sleep(random.randint(5, 10))
                    except Exception as e:
                        print(e)
                        continue
with open(r'.\spider\fault_urls.txt', 'w', encoding='utf-8') as f:
    for url in fault_urls:
        f.write(url + '\n')

