import requests
from my_fake_useragent import UserAgent
import re
list = ['2010%E5%B9%B4%E4%BB%A3', 2019, 2020, 2021, 2022, 2023]
for i in list:
    url = f'https://m.douban.com/rexxar/api/v2/movie/recommend?refresh=0&start=0&count=20&selected_categories=%7B%7D&uncollect=false&tags={i}&ck=Q0Fp&for_mobile=1'
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
