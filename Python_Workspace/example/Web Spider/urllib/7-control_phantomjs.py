# -*- coding:utf-8 -*-
# time:2019/03/03 15:58

from selenium import webdriver
import time
import datetime

start = datetime.datetime.now()

# 创建浏览器对象
browser = webdriver.PhantomJS(executable_path=r'E:\Python37\example\Web Spider\phantomjs-2.1.1-windows\bin\phantomjs.exe')

# 打开百度
url = "http://www.baidu.com/"
browser.get(url)
time.sleep(3)
browser.save_screenshot(r'E:\Python37\example\Web Spider\phantomjs\baidu.png')
time.sleep(3)

# 查找input输入框
my_input = browser.find_element_by_id('kw')
# 往框里写内容
my_input.send_keys('美女')
time.sleep(3)
browser.save_screenshot(r'E:\Python37\example\Web Spider\phantomjs\meinv.png')
time.sleep(3)

# 查找搜索按钮
# button = browser.find_elements_by_class_name('bg s_btn')[0]
button = browser.find_element_by_id('su')
# 点击一下搜索
button.click()
time.sleep(3)
browser.save_screenshot(r'E:\Python37\example\Web Spider\phantomjs\ssss.png')
time.sleep(3)

browser.quit()



end = datetime.datetime.now()
print("[ Finished in", (end - start) ,"]")