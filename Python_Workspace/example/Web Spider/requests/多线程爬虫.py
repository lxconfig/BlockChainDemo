# -*- coding:utf-8 -*-
# time: 2019/05/09 19:27
# File: 多线程爬虫.py
"""
1.两类线程：
    爬取线程，主要用来爬取页面的源代码
    分析线程，主要用来分析代码中的数据，提取数据并保存到文件中
2.用Queue存放源代码，分析线程从Queue中取源代码
"""
import threading
from lxml import etree
from multiprocessing import Queue
import requests
import time
import csv
import os


def spider_content(url, queue):
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    }
    response = requests.get(url=url, headers=headers)
    queue.put(response.text)
    # print(queue.get())

def analysis_content(queue, data, item):
    headers = ["标题", "朝代", "作者", "诗文"]
    data.append(item)
    while True:
        content = queue.get()
        tree = etree.HTML(content)
        div_list = tree.xpath("//div[@class='left']//div[@class='sons']")
        for div in div_list:
            item["标题"] = div.xpath("./div/p[1]/a/b/text()")[0]
            item["朝代"] = div.xpath("./div/p[2]/a[1]/text()")[0]
            item["作者"] = div.xpath("./div/p[2]/a[2]/text()")[0]
            item["诗文"] = div.xpath("./div/div[@class='contson']//text()")
            write_2_excel(headers, data)
        if queue.empty():
            break

def write_2_excel(headers, data):
    file_name = "poem.csv"
    with open(file_name, 'w', newline="") as fps:
        csv_DictWriter = csv.DictWriter(fps, headers)
        csv_DictWriter.writeheader()

    with open(file_name, "r") as f:
        csv_reader = csv.reader(f)
        list1 = [row for row in csv_reader]
        with open(file_name, "a+", newline="") as fp:
            csv_DictWriters = csv.DictWriter(fp, headers)
            if list1[0] == headers:
                for rows in data:
                    csv_DictWriters.writerow(rows)

def main():
    start_url = "https://www.gushiwen.org/"
    data = list()
    item = dict()
    # 创建队列
    queue = Queue()
    # 创建线程
    spider_thread = threading.Thread(target=spider_content, args=(start_url, queue))
    analysis_thread = threading.Thread(target=analysis_content, args=(queue, data, item))
    # 启动线程
    spider_thread.start()
    analysis_thread.start()

if __name__ == '__main__':
    main()