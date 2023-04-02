from bs4 import BeautifulSoup
import re
import requests
url='https://www.bilibili.com/video/BV1Sk4y1471G/?spm_id_from=333.1007.tianma.1-1-1.click'
content=requests.get(url).text
soup=BeautifulSoup(content,'html.parser')
title=soup.title.string
print(title)
paragraphs=soup.findAll('p')
for p in paragraphs:
    print(p.string)