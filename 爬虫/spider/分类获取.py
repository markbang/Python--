# 打开大众点评网址，选择上海地区的美食分类，获取所有美食分类编号，用selenium

from selenium import webdriver

# 打开浏览器
driver = webdriver.Chrome()
# 打开网址
driver.get('http://www.dianping.com/shanghai/ch10')
# 读取cookie信息，如果没有，登录之后保存cookie信息

# 点击更多加载全部分类
driver.find_element('css', 'a.J_packup.more').click()