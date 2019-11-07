# -*- coding:utf-8 -*-
# time:2018/12/20 15:37
import urllib.request
import urllib.parse
import re
import os
import time

def handle_request(url, page):
    url = url + str(page) + '/'
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    }
    request = urllib.request.Request(url, headers=headers)
    return request

def download_image(content):
    pattern = re.compile(r'<div class="thumb">.*?<img src="(.*?)" .*?>.*?</div>', re.S)
    lt = pattern.findall(content)
    print(lt)
    # 遍历列表，依次下载图片
    for image_src in lt:
        # 先处理image_src
        image_src = 'https:' + image_src
        # 发送请求，下载图片
        # 创建文件夹
        dirname = 'qiutu'
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        filename = image_src.split('/')[-1]
        path = dirname + '/' + filename
        print('%s图片正在下载...' % filename)
        urllib.request.urlretrieve(image_src, path)
        print('%s图片结束下载...' % filename)
        time.sleep(2)

def main():
    url = 'https://www.qiushibaike.com/pic/page/'
    start_page = int(input('请输入起始页码:'))
    end_page = int(input('请输入结束页码:'))
    for page in range(start_page, end_page + 1):
        print('第%s页开始下载...' % page)
        # 生成请求对象
        request = handle_request(url, page)
        # 发送请求对象，获取响应内容
        content = urllib.request.urlopen(request).read().decode()
        # 解析内容，提取所有图片链接，下载图片
        download_image(content)
        print('第%s页下载完毕...' % page)
        time.sleep(1)

if __name__ == '__main__':
    main()