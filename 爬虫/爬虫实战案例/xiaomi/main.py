import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
path = 'C:/Users/LENOVO/Desktop/Python文件/爬虫/爬虫实战案例/xiaomi/43.mp4'
def createFromData(data, path):
    encode = MultipartEncoder(
        fields={
            'file': (data['file_name'], open(path, 'rb'), data['file_type']),
            "uid": uid,
            "pid": pid,
            'type': 'msg',
            'countTag': "1",
            'source': "0",
        },
        boundary='----WebKitFormBoundarywbUvCVnu0gz0hs7s'
    )
    return encode
def createData(path):
    file_name = path.rsplit('/', 1)[1]
    with open(path, 'rb') as file:
        size = str(len(file.read()))
    ext = file_name.split('.', 1)[1]
    temp_type = f'image/{ext}'
    return {
        'file_name': file_name,
        'file_size': size,
        'file_type': temp_type
    }
url = "https://api-c.sobot.com/text/chat-visit/user/init.action"
payload = "ack=1&sysNum=5d7e332c4f994cf295cbfb0e81851038&source=0&chooseAdminId=&tranFlag=0&groupId=&partnerId=&tel=&email=&uname=&visitTitle=&visitUrl=&face=&realname=&weibo=&weixin=&qq=&sex=&birthday=&remark=&params=&isReComment=1&customerFields=&visitStartTime=&multiParams=&summaryParams=&channelFlag=2&isVip=&vipLevel=&userLabel=&xst=&isJs=0&joinType="
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https",
    "Referer": "https",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "bNo": "5d7e332c4f994cf295cbfb0e81851038",
    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
response = requests.post(url, data=payload, headers=headers)
co_li = [response.headers["Set-Cookie"].split(" ")[0], response.headers["Set-Cookie"].split(" ")[3].replace("path=/;HttpOnly;Max-Age=1800,", ""), response.headers["Set-Cookie"].split(" ")[4]]
cookie = " ".join(co_li)
headers1 = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": createData(path)['file_size'],
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarywbUvCVnu0gz0hs7s",
    "Cookie": cookie,
    "Origin": "https://www.sobot.com",
    "Host": "www.sobot.com",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "X-Requested-With": "XMLHttpRequest"
}
uid = response.json()['uid']
pid = response.json()['pid']
data = createData(path)
from_data = createFromData(data, path)
data = from_data
url = 'https://www.sobot.com//chat-web-upload/webchat/fileUploadForPostMsgBypc'
response1 = requests.post(url, data=data, headers=headers1)
print(response1.text)