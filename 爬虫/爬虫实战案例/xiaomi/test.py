import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

def bootstrap():
    path = 'C:/Users/LENOVO/Desktop/Python文件/爬虫/爬虫实战案例/xiaomi/test.jpg'
    # path = 'C:/Users/i/Pictures/壁纸9.jpg'
    data = createData(path)
    from_data = createFromData(data, path)
    res = upload(from_data, data)
    print(res['data'][0]['olink'])
# def

def createData(path):
    file_name = path.rsplit('/', 1)[1]
    with open(path, 'rb') as file:
        size = len(file.read())
    headers = {
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryzROqT4L0VBRUihWb',
        'Content-Length': str(size),
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    ext = file_name.split('.', 1)[1]
    temp_type = f'image/{ext}'
    return {
        'file_name': file_name,
        'headers': headers,
        'file_type': temp_type
    }
    pass

def createFromData(data, path):
    encode = MultipartEncoder(
        fields={
            'file': (data['file_name'], open(path, 'rb'), data['file_type'])
        },
        boundary='----WebKitFormBoundaryzROqT4L0VBRUihWb'
    )
    return encode

def upload(from_data, data):
    url = 'https://maoyan.com/ajax/proxy/admin/mmdb/photos/upload.json'
    response = requests.post(url, data=from_data, headers=data['headers'])
    result = response.json()
    return result

if __name__ == '__main__':
    bootstrap()