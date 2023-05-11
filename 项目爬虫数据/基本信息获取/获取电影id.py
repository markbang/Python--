# 根据豆瓣自己的综合排序，获取2010年代、2019年、2020年、2021年、2022年、2023年的排名前20的电影id
import requests
from my_fake_useragent import UserAgent
import re
# 这里的2010年代，需要转换成url编码，否则会报错，所以我直接复制过来了
movie_list = ['2010%E5%B9%B4%E4%BB%A3', 2019, 2020, 2021, 2022, 2023]
for i in movie_list:
    url = f'https://m.douban.com/rexxar/api/v2/movie/recommend?refresh=0&start=0&count=20&selected_categories=%7B%7D&uncollect=false&tags={i}&ck=Q0Fp&for_mobile=1'
    # heraders中的Referer是必须的，否则会返回出错信息，这个也是项目快做完时我才发现的，一开始是复制浏览器中的preview才开始爬虫的
    # 所以会看到详细信息里面的电影id.txt，那个是之前程序生成的，不是这个程序生成的，现在这个程序是对项目的一个优化
    headers = {
        'User-Agent': UserAgent().random(),
        'Referer': 'https://movie.douban.com/explore',
    }
    response = requests.get(url, headers=headers)
    obj = re.compile(r'"id": "(?P<movie_id>\w*?)", "title"')
    movie_id_list = obj.findall(response.text)
    for movie_id in movie_id_list:
        with open('movie_id.txt', 'a', encoding='utf-8') as f:
            f.write(movie_id + '\n')
            f.close()