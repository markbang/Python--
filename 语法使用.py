import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
elem.send_keys("python",Keys.ENTER)
time.sleep(3)
print(driver.page_source)
