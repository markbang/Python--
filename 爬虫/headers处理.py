import requests
import json
import random
import time
from my_fake_useragent import UserAgent
import re
from bs4 import BeautifulSoup
from lxml import etree
url = 'https://m.douban.com/rexxar/api/v2/movie/recommend?refresh=0&start=0&count=20&selected_categories=%7B%7D&uncollect=false&tags=2022&ck=Q0Fp&for_mobile=1'
headers = {
    'User-Agent': UserAgent().random(),
    'Referer': 'https://movie.douban.com/explore',
}
response = requests.get(url, headers=headers)