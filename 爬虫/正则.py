from urllib.parse import urlencode
import requests
import time
import csv
base_url='https://m.douban.com/'
data={"msg": "invalid_request_1284", "code": 1287, "request": "GET \/rexxar\/v2\/movie\/recommend", "localized_message": ""}
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}
url=base_url+urlencode(data)
res=requests.get(url,headers=headers).text
print(res)