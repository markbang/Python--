# 根据电影id爬取豆瓣影评
import requests
import re
import time
import random
from my_fake_useragent import UserAgent
import pandas as pd
movie_name=input('请输入豆瓣电影名称：')
with open(r'C:\Users\LENOVO\Desktop\Python文件\项目爬虫\详细信息(包括电影评价人数、评分等)\电影id.txt','r',encoding='utf-8') as f:
    movie_dic=eval(f.read())
    movie_id=movie_dic[movie_name]
# 豆瓣短评用网址只能看到前30页
for i in range(16,31):
    url='https://movie.douban.com/subject/'+str(movie_id)+f'/comments?start={i*20}&limit=20&status=P&sort=new_score'
    ua = UserAgent(family='chrome')
    res=ua.random()
    headers = {'User-Agent': res,
               'cookie':'ll="108296"; bid=C-dI_V2TQ1c; __yadk_uid=qDN9TQ26cWwTcU3pvLZdNTVM8BOmQM2u; _vwo_uuid_v2=D898B41559BCC3A84543E5E8D9CF64F73|aff5d7ee22cdec14c5dc9e4d2c0a1909; __gads=ID=1e84fadeb415b588-22c51e5e4adf00a9:T=1682001018:RT=1682001018:S=ALNI_MZQAZ56ylRX1WsdwEdNXzWNVK7fZg; __utmz=30149280.1682132050.4.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmz=223695111.1682132050.3.2.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=r'
                        'eferral|utmcct=/; __gpi=UID=00000bf0454ee5a4:T=1681130582:RT=1682132733:S=ALNI_MawBtRXAclTas-kDBdzYp9h-2z6KA; Hm_lvt_16a14f3002af32bf3a75dfe352478639=1681997153,1682133657; __utma=30149280.443719266.1681130582.1682132050.1682136844.5; __utma=223695111.1534656059.1681997132.1682132050.1682136844.4; _pk_ref.100001.4cf6=["","",1682143124,"https://cn.bing.com/"]; _pk_id.100001.4cf6=e945a3ba2e712c79.1682000945.4.1682143125.1682080198.; _ga=GA1.2.443719266.1681130582; douban-fav-remind=1; dbcl2="270334106:bSmIeq0yb0Q"; push_noty_num=0; push_doumail_num=0; ct=y; ck=Q0Fp; frodotk_db="59e7ff84f1120e410db7fe8ed3362ac3"'}
    response=requests.get(url,headers=headers)
    obj=re.compile(r'<span class="comment-location">(?P<location>.*?)</span>.*?<span class="short">(?P<comment>.*?)</span>',re.S)
    content=obj.finditer(response.text)
    print('正在爬取第'+str(i+1)+'页')
    for item in content:
        # 有些评论没有地区，可能是因为豆瓣时间问题，最新评论都有地区
        location=item.group('location')
        comment=item.group('comment')
        print(location,comment)
        coln=['地区','评论']
        df=pd.DataFrame(columns=coln)
        df.loc[0]=[location,comment]
        df.to_csv(f'{movie_name}评论.csv',encoding='utf-8',index=False,mode='a',header=False)
    time.sleep(random.randint(3,6))
# 下面的是按时间排序的，还能够上选出来一些评论，但只能看到前10页
for i in range(0,11):
    url='https://movie.douban.com/subject/'+str(movie_id)+f'/comments?start={i*20}&limit=20&status=P&sort=time'
    ua = UserAgent(family='chrome')
    res=ua.random()
    headers = {'User-Agent': res,
               'cookie':'ll="108296"; bid=C-dI_V2TQ1c; __yadk_uid=qDN9TQ26cWwTcU3pvLZdNTVM8BOmQM2u; _vwo_uuid_v2=D898B41559BCC3A84543E5E8D9CF64F73|aff5d7ee22cdec14c5dc9e4d2c0a1909; __gads=ID=1e84fadeb415b588-22c51e5e4adf00a9:T=1682001018:RT=1682001018:S=ALNI_MZQAZ56ylRX1WsdwEdNXzWNVK7fZg; __utmz=30149280.1682132050.4.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmz=223695111.1682132050.3.2.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=r'
                        'eferral|utmcct=/; __gpi=UID=00000bf0454ee5a4:T=1681130582:RT=1682132733:S=ALNI_MawBtRXAclTas-kDBdzYp9h-2z6KA; Hm_lvt_16a14f3002af32bf3a75dfe352478639=1681997153,1682133657; __utma=30149280.443719266.1681130582.1682132050.1682136844.5; __utma=223695111.1534656059.1681997132.1682132050.1682136844.4; _pk_ref.100001.4cf6=["","",1682143124,"https://cn.bing.com/"]; _pk_id.100001.4cf6=e945a3ba2e712c79.1682000945.4.1682143125.1682080198.; _ga=GA1.2.443719266.1681130582; douban-fav-remind=1; dbcl2="270334106:bSmIeq0yb0Q"; push_noty_num=0; push_doumail_num=0; ct=y; ck=Q0Fp; frodotk_db="59e7ff84f1120e410db7fe8ed3362ac3"'}
    response=requests.get(url,headers=headers)
    obj=re.compile(r'<span class="comment-location">(?P<location>.*?)</span>.*?<span class="short">(?P<comment>.*?)</span>',re.S)
    content=obj.finditer(response.text)
    print('正在爬取第'+str(i+1)+'页')
    for item in content:
        location=item.group('location')
        comment=item.group('comment')
        print(location,comment)
        coln=['地区','评论']
        df=pd.DataFrame(columns=coln)
        df.loc[0]=[location,comment]
        df.to_csv(f'{movie_name}评论.csv',encoding='utf-8',index=False,mode='a',header=False)
    time.sleep(random.randint(3,6))
# 算下来，每部电影能爬800条评论，对于数据分析可能没那么精准，但也基本差不多了