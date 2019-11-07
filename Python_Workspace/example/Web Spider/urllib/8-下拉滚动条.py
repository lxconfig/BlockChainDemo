# -*- coding:utf-8 -*-
# time:2019/03/03 16:46
import datetime
from selenium import webdriver
import time

start = datetime.datetime.now()

# 浏览器对象
browser = webdriver.PhantomJS(executable_path=r'E:\Python37\example\Web Spider\phantomjs-2.1.1-windows\bin\phantomjs.exe')

url = "https://movie.douban.com/typerank?type_name=%E7%88%B1%E6%83%85&type=13&interval_id=100:90&action="
browser.get(url)
time.sleep(3)

browser.save_screenshot(r'E:\Python37\example\Web Spider\phantomjs\douban_movie1.png')
# time.sleep(3)

# 让browser执行简单的js代码，模拟滚动条滚动到底部
js = 'document.body.scrollTop = 10000'
browser.execute_script(js)
time.sleep(10)
browser.save_screenshot(r'E:\Python37\example\Web Spider\phantomjs\douban_movie2.png')

# 获取网页代码，保存到文件中
html = browser.page_source
with open(r"E:\Python37\example\Web Spider\phantomjs\douban.html", 'w', encoding="utf8") as f:
    f.write(html)




browser.quit()















end = datetime.datetime.now()
print("[ Finished in", (end - start), "]")