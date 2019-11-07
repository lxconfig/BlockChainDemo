# -*- coding:utf-8 -*-
# time:2019/02/25 14:17
import urllib.request
import urllib.parse
from lxml import etree
import os.path
import time

# 处理url，发送情求
def handle_request(url, page):
    if page == 1:
        url = url.format('')
    else :
        url = url.format("_" + str(page))
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    }
    request = urllib.request.Request(url, headers=headers)
    return request

def parse_content(content):
    tree = etree.HTML(content)
    image_list = tree.xpath('//div[@class="box picblock col3"]/div/a/img/@src2')
    for image_src in image_list:
        # 下载每张图片
        download_image(image_src)

def download_image(image_src):
    dir_path = "美食图片"
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    # 文件(图片)名
    file_name = image_src.split('/')[-1]
    # file_name = os.path.basename(image_src)
    # 图片路径
    image_path = dir_path + '\\' + file_name
    # image_path = os.path.join(dir_path, file_name)
    # 发送下载图片的请求
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    }
    request = urllib.request.Request(image_src, headers=headers)
    response = urllib.request.urlopen(request).read()
    with open(image_path, 'wb') as f:
        f.write(response)

def main():
    url = "http://sc.chinaz.com/tupian/meishi{}.html"
    start_page = int(input("请输入开始页码："))
    end_page = int(input("请输入结束页码："))
    for page in range(start_page, end_page + 1):
        # 对每个page都发送请求
        print("开始读取第%s页的图片" % page)
        request = handle_request(url, page)
        content = urllib.request.urlopen(request).read().decode()
        # 解析服务器发回的内容
        parse_content(content)
        print("第%s页的图片下载完成" % page)
        time.sleep(2)


if __name__ == '__main__':
    main()