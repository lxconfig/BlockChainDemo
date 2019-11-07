# -*- coding:utf-8 -*-
# time:2019/03/01 20:08

from selenium import webdriver
import time

# 模拟创建一个浏览器对象，通过对象操作浏览器
'''
# 打开浏览器
path = r'E:\Python37\example\Web Spider\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path)

# 浏览器打开url
url = "http://www.baidu.com"
browser.get(url)
time.sleep(1)

# 查找input输入框
my_input = browser.find_element_by_id('kw')
# 往框里写内容
my_input.send_keys('美女')
time.sleep(1)

# 查找搜索按钮
# button = browser.find_elements_by_class_name('bg s_btn')[0]
button = browser.find_element_by_id('su')
# 点击一下搜索
button.click()
time.sleep(3)

# 找到指定图片点击
image = browser.find_elements_by_class_name('op-img-address-link-imgs')[1]
image.click()
time.sleep(3)
# 关闭浏览器
browser.quit()
'''

# 创建浏览器对象，打开浏览器窗口
browser = webdriver.Chrome(executable_path=r"E:\Python37\example\Web Spider\chromedriver.exe")

# 打开指定网页
url = "https://www.douyu.com/"
browser.get(url)
time.sleep(2)

# 查找页面内指定内容，并点击打开
room = browser.find_elements_by_class_name("DyCover ")[1].click()
time.sleep(10)

# 关闭浏览器
browser.close()