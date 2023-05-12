import requests
from my_fake_useragent import UserAgent

def get_html(url):
    data = {
        'limit': 20,
        'current': 2,
        'pubDateStartTime':'',
        'pubDateEndTime': '',
        'prodPcatid': '',
        'prodCatid':'',
        'prodName':''
    }
    headers= {
        'User-Agent': UserAgent().random(),
        'Referer': 'http://www.xinfadi.com.cn/priceDetail.html',
        'X-Requested-With': 'XMLHttpRequest',

        'Connection': 'keep-alive',
    }
    html = requests.post(url, data=data, headers=headers)
    html.encoding = 'utf-8'
    return html.text

if __name__ == '__main__':
    url = 'http://www.xinfadi.com.cn/priceDetail.html'
    html = get_html(url)
    print(html)
