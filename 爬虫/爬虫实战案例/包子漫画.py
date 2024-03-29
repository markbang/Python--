import asyncio
import aiohttp
import requests
from lxml import etree

headers = {
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Accept': '*/*',
   'Host': 'cn.baozimh.one',
   'Connection': 'keep-alive'
}

response = requests.request("GET", "https://cn.baozimh.one/chapterlist/yirenzhixiafanwaixiutie-dongmantang", headers=headers)

html = etree.HTML(response.text)
_urls = html.xpath('//div[@class="chapteritem w-full md:w-1/2"]/a/@href')
urls = ['https://cn.baozimh.one' + url for url in _urls]
print(urls)
async def fetch_page(session, url):
    async with session.get(url) as response:
        return await response.text()
async def main(urls):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Accept': '*/*',
        'Host': 'cn.baozimh.one',
        'Connection': 'keep-alive'
    }
    urls_list = []
    async with aiohttp.ClientSession(headers=headers) as session:
        tasks = [fetch_page(session, url) for url in urls]
        pages = await asyncio.gather(*tasks)
        for page in pages:
            etree_html = etree.HTML(page)
            img_url = etree_html.xpath('//div[@class="w-full h-full"]/img/@data-src')
            # for i in img_url:
            #     img_url1 = i.replace("2.jpg", "1.jpg") if i.endswith("2.jpg") else ' '
            #     break
            img_li = list(img_url)
            chapter_name = etree_html.xpath('//h1[@class="text-center px-2 pt-8 font-semibold"]/text()')
            chapter_li = list(chapter_name)
            urls_list = urls_list + chapter_li + img_li
        with open("urls.md", "w", encoding='utf-8') as f:
            for url in urls_list:
                if not url.startswith("https"):
                    f.write(":::" + "\n")
                    f.write(f"## {url}" + "\n")
                    f.write("::: details 点击展开" + "\n")
                else:
                    f.write(f"![]({url})" + "\n")
            f.write(":::" + "\n")
        with open("urls.md", "r", encoding='utf-8') as f:
            lines = f.readlines()
        if lines:
            del lines[0]
            with open("urls.md", "w", encoding='utf-8') as f:
                f.writelines(lines)
            

asyncio.run(main(urls))

