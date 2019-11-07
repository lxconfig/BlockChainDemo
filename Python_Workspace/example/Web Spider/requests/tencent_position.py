# -*- coding:utf-8 -*-
# time: 2019/04/29 18:59
# File: tencent_position.py
"""
1. 采用selenium+phantomjs完成指定工作的爬取
2. 获取响应内容
3. 自动翻页获取下一页数据
4. 数据存入csv中
"""

from selenium import webdriver
import requests
import csv
import time
from lxml import etree


def Spider_Phantomjs(start_url, kw):
    '''自动化输入职位查找'''
    # 创建browser对象
    browser = webdriver.PhantomJS(executable_path=r'phantomjs.exe')
    # 打开招聘网站
    url = start_url
    browser.get(url)
    # 找到输入框
    keywords = browser.find_element_by_class_name("search-input input-value")
    keywords.send_keys(kw)
    # 找到搜索框
    submit = browser.find_element_by_class_name("search-btn")
    # 点击搜索
    submit.click()
    time.sleep(10)
    content =  browser.page_source
    browser.quit()
    return content

def parse_content(content):
    '''提取页面数据'''
    tree = etree.HTML(content)
    div_list = tree.xpath('//div[@class="correlation-degree"]/div/div')  # 除第一个和最后一个其他tr都要
    for div in div_list:
        item = {}
        item["职位名称"] = div.xpath('./a/h4/text()')[0]
        item["工作地点"] = div.xpath('./a/p[1]/span[2]/text()')[0]
        item["工作性质"] = div.xpath('./a/p[1]/span[3]/text()')[0]
        item["工作描述"] = div.xpath('./a/p[2]/text()')[0]
        item["发布时间"] = div.xpath('./a/p[1]/span[4]/text()')[0]
        return item

def main():
    kw = input("请输入要查找的职位：")
    start_url = "https://careers.tencent.com/home.html"
    content = Spider_Phantomjs(start_url, kw)
    item = parse_content(content)
    print(item)
    


if __name__ == '__main__':
    main()