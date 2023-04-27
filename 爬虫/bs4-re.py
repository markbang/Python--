import re
import requests
from selenium import webdriver
import time
browser=webdriver.Chrome()
browser.get(r'https://movie.douban.com/explore')
time.sleep(2)
print(browser.title)
print(browser.current_url)
print(browser.name)
print(browser.page_source)

browser.close()