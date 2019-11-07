# -*- coding:utf-8 -*-
# time:2018/12/21 14:22

# 需求：爬取某一页、某几页的全部图片

import urllib.request
import urllib.parse
import re
import os

def handle_url(url, page):
    url = url + str(page) + '/'
    return url

def download_image(response):
    pattern = re.compile(r'<div class="thumb">.*?<img src="(.*?)" .*?>.*?</div>', re.S)
    ret = pattern.findall(response)
    for image_url in ret:
        image_url = 'https:' + image_url
        file_name = image_url.split('/')[-1]
        path = "qiutu" + '\\' + file_name
        if not os.path.exists("qiutu"):
            os.mkdir("qiutu")
        print("%s张图片正在下载..." % file_name)
        urllib.request.urlretrieve(image_url, path)
        print("%s张图片下载完成..." % file_name)

def main():
    url = "https://www.qiushibaike.com/imgrank/page/"
    start_page = int(input("请输入开始页码："))
    end_page = int(input("请输入结束页码："))
    for page in range(start_page, end_page + 1):
        # 处理url，把页数拼接上去
        url1 = handle_url(url, page)
        # 构建请求对象
        headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        }
        print("第%s页开始读取..." % page)
        request = urllib.request.Request(url1, headers=headers)
        # 发送请求
        response = urllib.request.urlopen(request).read().decode()
        download_image(response)
        print("第%s页结束读取..." % page)

if __name__ == '__main__':
    main()

