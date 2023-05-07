# 根据电影id爬取豆瓣影评
import requests
from bs4 import BeautifulSoup
import time
import random
from my_fake_useragent import UserAgent
import pandas as pd
movie_id=input('请输入豆瓣电影名称：')
with open(r'C:\Users\LENOVO\Desktop\Python文件\项目爬虫\详细信息(包括电影评价人数、评分等)\电影id.txt','r',encoding='utf-8') as f:
    movie_dic=eval(f.read())
    movie_id=movie_dic[movie_id]
for i in range(0,10000):
    url='https://movie.douban.com/subject/'+str(movie_id)+f'/comments?start={i*20}&limit=20&status=P&sort=new_score'
    ua = UserAgent(family='chrome')
    res=ua.random()
    headers = {'User-Agent': res,
                'cookie':'ll="108296"; bid=C-dI_V2TQ1c; __gads=ID=1e84fadeb415b588-22c51e5e4adf00a9:T=1682001018:RT=1682001018:S=ALNI_MZQAZ56ylRX1WsdwEdNXzWNVK7fZg; __utmz=30149280.1682132050.4.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __gpi=UID=00000bf0454ee5a4:T=1681130582:RT=1682132733:S=ALNI_MawBtRXAclTas-kDBdzYp9h-2z6KA; __ut'
                         'ma=30149280.443719266.1681130582.1682132050.1682136844.5; _ga=GA1.2.443719266.1681130582; douban-fav-remind=1; dbcl2="270334106:bSmIeq0yb0Q"; push_noty_num=0; push_doumail_num=0; ct=y; ck=Q0Fp; frodotk_db="aec40ec1b81bda660c4c2c4528538f32"; ap_v=0,6.0'}
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.text,'html.parser')
    comment=soup.find_all('span',class_='short')
    print('正在爬取第'+str(i+1)+'页')
    for item in comment:
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
        with open(r'C:\Users\LENOVO\Desktop\Python文件\项目爬虫\详细信息(包括电影评价人数、评分等)\电影评论\深海评论.csv','a',encoding='utf-8') as f:
            pd.DataFrame([random_province,item.string]).T.to_csv(f,header=False,index=False)
        print(item.string)
    time.sleep(random.randint(5,10))