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
def fetch_comments(movie_id, start_index):
    import random
    i=0
    # 将爬取的评论存储在csv文件中,文件名为电影名称，第一列为顺序序号，第二列用random()函数生成随机中国地区，第三列为评论内容  # 随机选取一个IP
    url = f'https://movie.douban.com/subject/{movie_id}/reviews?start={start_index}'
    ua = UserAgent(family='chrome')
    res = ua.random()
    headers = {'User-Agent': res,
               "Connection": "close"}
    # with open('C:\\Users\\LENOVO\\Desktop\\Python文件\\项目爬虫\\详细信息(包括电影评价人数、评分等)\\proxy.txt', 'r') as f:
    #     proxies_pool = f.readlines()
    # proxy = random.choice(proxies_pool).strip()
    # proxies_pool=[{'http': 'http://'+ proxy,
    #     'https': 'http://'+ proxy}]
    proxies = {'https': '42.5.21.62:4315'}
    proxyhandler = request.ProxyHandler(proxies)
    opener = request.build_opener(proxyhandler)
    opener.addheaders = [('User-Agent', res)]
    request.install_opener(opener)
    response=request.urlopen(request.Request(url, headers=headers))
    content=response.read().decode('utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    comments = soup.find_all('div', class_='short-content')
    f = open(f'..\\项目爬虫\\详细信息(包括电影评价人数、评分等)\\电影评论\\{moive_name}.csv','w', encoding='utf-8', newline='')
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

# 该函数用于启动多线程进行爬取
def start_crawling(movie_id, comment_count, thread_count):
    threads = []
    for i in range(thread_count):
        start_index = i * (comment_count // thread_count)
        end_index = (i + 200) * (comment_count // thread_count) if i < thread_count - 1 else comment_count
        thread = threading.Thread(target=fetch_comments, args=(movie_id, start_index))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
# 读取本目录下电影id.txt文件，获取电影名称和id，电影id.txt为字典形式，key为电影名称，value为电影id
with open('电影id.txt', 'r', encoding='utf-8') as f:
    movie_id_dict = eval(f.read())
    f.close()
for key in movie_id_dict.keys():
    moive_name = key
# 指定要爬取的电影 ID、评论总数和线程数，然后启动多线程进行爬取
    movie_id = movie_id_dict[key]
    comment_count = 100
    thread_count = 5
    start_crawling(movie_id, comment_count, thread_count)

