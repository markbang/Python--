# 通过观察豆瓣电影网页，发现id对应网页，所以前面获取的id可以直接用来爬取评论
# 先根据每个id获取电影的名字、导演名称、电影类型、制片国家/地区、上映日期、片长、又名、评分、评价人数
# 再根据每个id获取电影的评论
import re
import requests
import pandas as pd
base_url='https://movie.douban.com/subject/'
movie_id_file=open('../详细信息(包括电影评价人数、评分等)/电影id.txt','r',encoding='utf-8')
movie_id=eval(movie_id_file.read())
movie_id_file.close()
n=0
for id in movie_id.values():
    headers={
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }
    url=base_url+str(id)+'/'
    res=requests.get(url,headers=headers).text
    obj=re.compile(r'<span property="v:itemreviewed">(?P<movie>.*?)</span>.*?<span class="year">\((?P<year>.*?)\)</span>'
                   r'.*?导演</span>.*?rel="v:directedBy">(?P<director>.*?)</a>.*?"v:genre">(?P<category1>.*?)</span>.*?'
                   r'"v:genre">(?P<category2>.*?)</span>.*?制片国家/地区:</span> (?P<country>.*?)<br/>.*?片长:</span>.*?">(?P<length>.*?)'
                   r'</span><br/>.*?"v:average">(?P<score>.*?)</strong>.*?<span property="v:votes">(?P<num>.*?)</span>人评价.*?',re.S)
    result=obj.finditer(res)
    for i in result:
        n+=1
        movie_name=i.group('movie')
        movie_year=i.group('year')
        movie_director=i.group('director')
        movie_category1=i.group('category1')
        movie_category2=i.group('category2')
        movie_country=i.group('country')
        movie_length=i.group('length')
        movie_score=i.group('score')
        movie_num=i.group('num')
        movie_category=movie_category1+movie_category2
        # 保存电影信息为csv文件，用pandas的DataFrame方法
        movie_info=pd.DataFrame({'电影名称':[movie_name],'上映年份':[movie_year],'导演':[movie_director],'电影类型':[movie_category],
                                 "制片国家/地区":[movie_country], '片长':[movie_length], '评分':[movie_score],
                                 "评价人数":[movie_num]})
        movie_info.to_csv('../详细信息.csv(包括电影评价人数、评分等)/电影信息.csv',mode='a',encoding='utf-8',index=False,header=False)
        print(f'电影信息爬取成功{n}')