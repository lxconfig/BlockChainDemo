# -*- coding:utf-8 -*-
# time:2019/03/04 15:25
import datetime
from selenium import webdriver
import time

start = datetime.datetime.now()

browser = webdriver.PhantomJS(r'E:\Python37\example\Web Spider\phantomjs-2.1.1-windows\bin\phantomjs.exe')

url = "http://sc.chinaz.com/tupian/beijingtupian.html"
browser.get(url)
time.sleep(3)
with open(r'E:\Python37\example\Web Spider\phantomjs\tupian1.html', 'w', encoding="utf8") as f:
    f.write(browser.page_source)

# 浏览后，图片才加载，src2变成src
js = 'document.body.scrollTop=10000'
browser.execute_script(js)
time.sleep(3)
with open(r'E:\Python37\example\Web Spider\phantomjs\tupian2.html', 'w', encoding="utf8") as f:
    f.write(browser.page_source)

browser.quit()











end = datetime.datetime.now()
print("[ Finished in", (end - start), "]")