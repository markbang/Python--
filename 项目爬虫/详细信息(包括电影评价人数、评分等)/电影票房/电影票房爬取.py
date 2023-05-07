#  由于豆瓣上没有电影票房信息，所以这里使用另一个网站(中国票房)来爬取的票房信息
#  分析这个网站之后，如果爬取指定电影的票房信息，无从下手，所以这里爬取近几年所有的电影票房信息，然后再与之前获得的电影信息进行匹配
import requests
import re
import time
import random
import pandas as pd
from my_fake_useragent import UserAgent
from bs4 import BeautifulSoup
for i in range(2010,2024):
    headers = {'User-Agent': UserAgent(family='chrome').random()}
    url=f'http://www.boxofficecn.com/boxoffice{str(i)}'
    response = requests.get(url, headers=headers)
    print(response.text)
# print(response.text)  发现可以输出网页源码，则就能得到该电影信息的网页
    # 通过正则表达式匹配出电影票房信息
    obj=re.compile(r'<a.*?">(?P<name1>.*?)</a>',re.S)
    time.sleep(random.randint(1, 3))
    content = BeautifulSoup(response.text, 'html.parser')
    matches = content.find_all('tr', align='left')
    for match in matches:
        name = match.find_all('td')[2].text
        box_office = match.find_all('td')[3].text
        if '重映' in name:
            name = name.split('（')[0]
        elif 'herf' in name:
            name=obj.search(name).group('name1')
        else:
            name = name
        if '（' in box_office:
            box_office = box_office.split('（')[0]
        else:
            box_office = box_office
        print(name, box_office)
        # 将爬取的数据保存到csv文件中
        df = pd.DataFrame({'name':[name],'box_office':[box_office]})
        df.to_csv(f'所有票房.csv', mode='a',index=False, encoding='utf-8',header=False)

