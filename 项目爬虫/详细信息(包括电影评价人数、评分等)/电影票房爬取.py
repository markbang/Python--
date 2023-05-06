#  由于豆瓣上没有电影票房信息，所以这里使用另一个网站https://ys.endata.cn/DataMarket/Index艺恩娱数来爬取的票房信息
#  分析这个网站之后，由于需要的是指定性的电影票房，所以现需要根据电影名字来爬取电影的id，然后根据电影id来爬取电影票房
import requests
import re
import time
import random
import pandas as pd
from my_fake_useragent import UserAgent
with open('电影id.txt', 'r', encoding='utf-8') as f:
    movie_names_dic = eval(f.read())
    f.close()
for movie_name in movie_names_dic.keys():
    params = {'key': movie_name}
    headers = {'User-Agent': UserAgent(family='chrome').random(),'cookie':'route=65389440feb63b53ee0576493abca26d'}
    url='https://ys.endata.cn/DataMarket/Search'
    response = requests.get(url, params=params, headers=headers)
    # print(response.text)  发现可以输出网页源码，则就能得到该电影信息的网页
    time.sleep(random.randint(1, 3))
obj=re.compile(r'<a href="/DataMarket/Detail/(\d+)" target="_blank" class="title">')
#  先定义一个函数，用来获取电影的id
# def get_movie_id(movie_name):
