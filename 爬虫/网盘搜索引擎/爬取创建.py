import requests
import re
from my_fake_useragent import UserAgent


def get_html(url):
    try:
        ua = UserAgent()
        headers = {'User-Agent': ua.random(), 'Referer': 'https://www.upyunso.com/'}  # 伪装浏览器
        r = requests.get(url, timeout=30, headers=headers)
        r.raise_for_status()  # 如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding  # 用内容编码替换响应头编码
        return r.text
    except:
        return "产生异常"


print(get_html('https://www.upyunso.com/search.html?keyword=%E8%8B%B1%E8%AF%AD&page=2&s_type=2'))