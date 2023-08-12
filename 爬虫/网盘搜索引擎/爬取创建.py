import requests
import re
from my_fake_useragent import UserAgent


def get_html(url):
    try:
        ua = UserAgent()
        headers = {'User-Agent': ua.random(),'Cookies':'close_menu=false; bookstack=b79e4f980ec5775d45aeeb45eb73cd2c; iamadmin=true',
                   'Referer':'https://www.bookstack.cn/books/Python-100-Days'}  # 伪装浏览器
        r = requests.get(url, timeout=30, headers=headers)
        r.raise_for_status()  # 如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding  # 用内容编码替换响应头编码
        return r.text
    except:
        return "产生异常"


print(get_html('https://www.bookstack.cn/read/Python-100-Days/spilt.1.Day16-20-16-20.Python%E8%AF%AD%E8%A8%80%E8%BF%9B%E9%98%B6.md'))