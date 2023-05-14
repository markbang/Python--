import pandas as pd
import requests
from my_fake_useragent import UserAgent
import json
from concurrent.futures import ThreadPoolExecutor
import time
import random
# 原始网页 http://www.xinfadi.com.cn/priceDetail.html


def get_html(page):
    url = 'http://www.xinfadi.com.cn/getPriceData.html'
    headers = {
        'User-Agent': UserAgent().random()
    }
    data = {'current': page}
    response = requests.post(url, data=data, headers=headers)
    response.encoding = 'utf-8'
    json_data = json.loads(response.text)
    for i in json_data['list']:
        df = pd.DataFrame([i])
        df.to_csv('蔬菜价格.csv', mode='a', encoding='utf-8', index=False, header=False)
    print('第{}页爬取完成'.format(page))
    time.sleep(random.randint(5, 10))


if __name__ == '__main__':
    with ThreadPoolExecutor(100) as pool:
        for i in range(1, 5001):
            pool.submit(get_html, i)