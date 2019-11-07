# -*- coding:utf-8 -*-
# time:2019/02/25 10:51

import urllib.request
import urllib.parse
from lxml import etree
import time
import os

# 发送请求
def handle_request(url, page):
    if page == 1:
        url = url.format('','')
    else:
        url = url.format('_', str(page))
        # url = url.format('_' + str(page))  # 对应url_1
    # 构建请求对象，发送请求
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    }
    request = urllib.request.Request(url, headers=headers)
    return request

# 解析内容，下载图片
def parse_content(content):
    tree = etree.HTML(content)
    # 懒加载技术：用到的时候才加载
    # 实现方法：<img src2="图片路径">,通过js，动态的给img添加src属性，<img src="图片路径" src2="图片路径">
    image_url_list = tree.xpath('//div[@class = "box picblock col3"]/div/a/img/@src2')
    # 遍历列表，依次下载图片
    for image_src in image_url_list:
        download_image(image_src)

def download_image(image_src):
    dir_name = "风景图片"
    # 创建文件夹，如存在则跳过
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    # 图片的文件名
    file_name = os.path.basename(image_src)
    # 图片路径
    file_path = os.path.join(dir_name, file_name)
    print(file_path)
    # 发送请求
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    }
    request = urllib.request.Request(image_src, headers=headers)
    response = urllib.request.urlopen(request)
    with open(file_path,'wb') as f:
        f.write(response.read())

def main():
    url = 'http://sc.chinaz.com/tupian/fengjingtupian{}{}.html'
    # url_1 = 'http://sc.chinaz.com/tupian/fengjingtupian{}.html'
    start_page = int(input("请输入开始页码："))
    end_page = int(input("请输入结束页码："))
    for page in range(start_page, end_page + 1):
        request = handle_request(url, page)
        # 获取响应
        content = urllib.request.urlopen(request).read().decode()
        # print(content)
        parse_content(content)
        time.sleep(2)

if __name__ == '__main__':
    main()