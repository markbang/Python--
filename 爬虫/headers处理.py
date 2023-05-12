import requests
from my_fake_useragent import UserAgent
from urllib.parse import urlencode
url = 'http://www.xinfadi.com.cn/priceDetail.html/limit=20&current=5&pubDateStartTime=&pubDateEndTime=&prodPcatid=&prodCatid=&prodName='
headers= {
    'User-Agent': UserAgent().random(),
    'Referer': 'http://www.xinfadi.com.cn/priceDetail.html',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}
# urlencode()将字典转换为url参数
html = requests.post(url, headers=headers)
html.encoding = 'utf-8'
print(html.text)