# -*- coding:utf-8 -*-
# time:2019/03/07 15:07
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

start = datetime.datetime.now()

# 创建一个参数对象，用来控制chrome以无界面模式打开
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# 创建浏览器对象
path = r'E:\Python37\example\Web Spider\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
# 上网
url = 'http://www.baidu.com/'
browser.get(url)
time.sleep(3)

browser.save_screenshot(r'E:\Python37\example\Web Spider\phantomjs\Headless_Chrome.png')

browser.quit()


end = datetime.datetime.now()
print("[ Finished in", (end - start), "]")