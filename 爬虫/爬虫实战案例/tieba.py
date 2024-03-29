import requests
# from lxml import html
# etree = html.etree
from lxml import etree
class Tieba(object):
    def __init__(self, name):
        self.url = f'https://tieba.baidu.com/f?kw={name}'
        self.headers = {
            'User-Agent': 'Baiduspider'
            # 'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) '     #  低端浏览器没有被<!--  -->注释掉
        }
 
    def get_data(self, url):
        response = requests.get(url, headers=self.headers)
        #  把浏览器响应的内容保存到本地，以便查看响应的源码
        # with open('tieba.html', 'wb') as f:
        #     f.write(response.content)
        return response.content
 
    def parse_data(self, data):
        #  创建element对象
        data = data.decode().replace("<!--", "").replace("-->", "")   #  高端浏览器会把一些内容给注释掉的
        el_html = etree.HTML(data)
        el_list = el_html.xpath('//*[@id="thread_list"]/li/div/div[2]/div[1]/div[1]/a')  #  此处输出的是对象
        print(len(el_list))
        data_list = []
        for el in el_list:
            tmp = {}
            tmp['title'] = el.xpath('./text()')[0]    #  此处xpath取出的数据是列表，所以加上索引[0]
            tmp['href'] = 'http://tieba.com' + el.xpath('./@href')[0]      #  此处取出的索引是相对路径，所以前面还要拼接字符串
            data_list.append(tmp)
        print(data_list)
        try:
            # next_url = 'https' + el_html.xpath('//a[@class="next pagination-item "]/@href')
            next_url = 'https:' + el_html.xpath('//a[contains(text(),"下一页")]/@href')[0]
        except:
            next_url = None
        return data_list, next_url
 
    def save_data(self, data_list):
        for data in data_list:
            print(data)
 
    def run(self):
        #  url
        #  headers
        next_url = self.url
        while True:
            #  发送请求，获取响应
            data = self.get_data(next_url)
            #  从响应中提取数据（数据和翻页用的url）
            data_list, next_url = self.parse_data(data)
            self.save_data(data_list)
            #  判断是否终结
            if next_url == None:
                break
 
 
if __name__ == '__main__':
    tieba = Tieba('一人之下')
    tieba.run()