#打开本目录下的逐个打开2023、2022、2021、2020、2019、10年代.txt,编写正则爬虫，获取电影id，“加写模式”将所有电影名字
# 和id以字典形式保存到文件中
import re
movie_id={}
for year in range(2023,2018,-1):
    movie_id_file=open('10年代.txt','r',encoding='utf-8')
    movie_id_file_read=movie_id_file.read()
    movie_id_file.close()
    obj=re.compile(r'"year":.*?"id": "(?P<id>.*?)",.*?"title": "(?P<name.txt>.*?)",',re.S)
    result=obj.finditer(movie_id_file_read)
    for i in result:
         movie_id[i.group('name.txt')]=i.group('id')
    print(movie_id)
    movie_id_file=open('../详细信息(包括电影评价人数、评分等)/电影id.txt', 'w', encoding='utf-8')
    movie_id_file.write(str(movie_id))
    movie_id_file.close()
