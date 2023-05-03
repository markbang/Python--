import requests
from bs4 import BeautifulSoup
import re
import csv
from my_fake_useragent import UserAgent
import time
# 该函数用于获取指定电影指定起始索引的评论信息
obj=re.compile(r'(?P<judge>.*?)\(展开\)',re.S)
import random
i=0
for i in range(0,100,20):
 # 将爬取的评论存储在csv文件中,文件名为电影名称，第一列为顺序序号，第二列用random()函数生成随机中国地区，第三列为评论内容  # 随机选取一个IP
    url = f'https://movie.douban.com/subject/35267208/reviews?start={i}'

    ua = UserAgent(family='chrome')
    res = ua.random()
    headers = {'User-Agent': res}
    # fieldname=[
    #     '36.6.144.28:8089',
    #     '47.100.90.127:6969',
    #     '49.86.176.138:8089',
    #     '223.247.46.137:8089',
    #     '1.116.7.221:3128',
    #     '120.26.50.145:8989']
    # proxy={'https:':random.choices(fieldname)}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    comments = soup.find_all('div', class_='short-content')
    f = open(f'..\\项目爬虫\\详细信息(包括电影评价人数、评分等)\\电影评论\\流浪地球2.csv','w', encoding='utf-8', newline='')
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
    time.sleep(3)
    f.close()
