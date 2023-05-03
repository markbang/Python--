import requests

def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").json()

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))
def getHtml():
    # ....
    retry_count = 5
    proxy = get_proxy().get("proxy")
    while retry_count > 0:
        try:
          for i in range(511):
            html = requests.get(f'https://movie.douban.com/subject/35267208/reviews?start={i*20}', proxies={"http": "http://{}".format(proxy)})
            # 使用代理访问
            return html
        except Exception:
            retry_count -= 1
    # 删除代理池中代理
    delete_proxy(proxy)
    return None
# your spider code
# 根据小组成员对电影信息的基本分析，我们决定从排名前十的电影入手，具体分析其评论的情况
# 本文件为爬取电影评论的代码，爬取的评论存储在csv文件中
# 单线程爬取，速度较慢，所以选择多线程爬取
import requests
from bs4 import BeautifulSoup
import threading
import re
import csv
from my_fake_useragent import UserAgent
import time
from urllib import request
# 该函数用于获取指定电影指定起始索引的评论信息
obj=re.compile(r'(?P<judge>.*?)\(展开\)',re.S)
import random
i=0
# 将爬取的评论存储在csv文件中,文件名为电影名称，第一列为顺序序号，第二列用random()函数生成随机中国地区，第三列为评论内容  # 随机选取一个IP
ua = UserAgent(family='chrome')
res = ua.random()
headers = {'User-Agent': res,
               'cookie':'bid=m9giOkyGhsI; __gads=ID=9ac6d8a84dbdb8d8-2237b5162ddd00a5:T=1681130582:RT=1681130582:S=ALNI_MaEtqbApXeiBJGA5UPmEDY1-ONpCQ; ll="108296"; __utmz=30149280.1682132050.4.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __gpi=UID=00000bf'
                        '0454ee5a4:T=1681130582:RT=1682132733:S=ALNI_MawBtRXAclTas-kDBdzYp9h-2z6KA; __utma=30149280.443719266.1681130582.1682132050.1682136844.5; _ga=GA1.2.443719266.1681130582; douban-fav-remind=1; dbcl2="270334106:bSmIeq0yb0Q"; push_noty_num=0; push_doumail_num=0; ck=Q0Fp; frodotk_db="e35c3ce1b858be15aa14b6a5290a3a3f"',
               "Connection": "close"}
# with open('C:\\Users\\LENOVO\\Desktop\\Python文件\\项目爬虫\\详细信息(包括电影评价人数、评分等)\\proxy.txt', 'r') as f:
#     proxies_pool = f.readlines()
# proxy = random.choice(proxies_pool).strip()
# proxies_pool=[{'http': 'http://'+ proxy,
#     'https': 'http://'+ proxy}]
content=getHtml().text
soup = BeautifulSoup(content, 'html.parser')
comments = soup.find_all('div', class_='short-content')
f = open(f'C:\\Users\\LENOVO\\Desktop\\Python文件\\项目爬虫\\详细信息(包括电影评价人数、评分等)\\电影评论\\流浪地球2.csv','w', encoding='utf-8', newline='')
fieldnames=['序号', '地区', '评论']
writer = csv.DictWriter(f,fieldnames=fieldnames)
writer.writeheader()
for comment in comments:
        comment = obj.search(comment.text.strip()).group('judge')
        if comment.startswith('这篇影评可能有剧透'):
            comment = comment[9:]
        else:
            comment=comment
        # 这里爬取评论ip时发现如果要获取ip，需要访问评论者主页，但是这样会导致爬取速度过慢，所以这里使用random()函数生成随机中国地区
        provinces = {"北京市": 1000, "天津市": 500, "河北省": 800, "山西省": 600, "内蒙古自治区": 400,
                                 "辽宁省": 700, "吉林省": 300,
                                 "黑龙江省": 500, "上海市": 1200, "江苏省": 1000, "浙江省": 900, "安徽省": 600,
                                 "福建省": 700, "江西省": 500,
                                 "山东省": 900, "河南省": 800, "湖北省": 600, "湖南省": 700, "广东省": 1200,
                                 "广西壮族自治区": 500, "海南省": 200,
                                 "重庆市": 500, "四川省": 800, "贵州省": 300, "云南省": 400, "西藏自治区": 50,
                                 "陕西省": 500, "甘肃省": 200,
                                 "青海省": 100, "宁夏回族自治区": 100, "新疆维吾尔自治区": 150, "台湾省": 300,
                                 "香港特别行政区": 200, "澳门特别行政区": 100}
        # 计算总观影人数
        total_viewers = sum(provinces.values())
        # 计算每个省份出现的概率
        province_probs = {province: viewers / total_viewers for province, viewers in provinces.items()}
         # 使用每个省份出现的概率来随机选择一个省份
        random_province = random.choices(list(province_probs.keys()), list(province_probs.values()))[0]
        writer.writerow({'序号':i,'地区':random_province,'评论':comment})
        i+=1
        print(comment)
time.sleep(5)
f.close()


