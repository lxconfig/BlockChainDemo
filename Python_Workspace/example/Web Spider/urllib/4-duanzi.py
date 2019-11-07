# -*- coding:utf-8 -*-
# time:2019/02/01 14:26

import urllib.request
import urllib.parse
from lxml import etree
import json
import time

class DuanZi:
    def __init__(self, start_page, end_page):
        self.start_page = start_page
        self.end_page = end_page
        self.url = "http://www.waduanzi.com/joke/page/"
        self.items = []

    # 处理url，发送请求
    def handle_request(self, page):
        get_url = self.url + str(page)
        # 构建请求对象，发送请求
        headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        }
        request = urllib.request.Request(get_url, headers= headers)
        return request

    # 处理响应内容
    def parse_content(self, content):
        # 利用xpath提取想要的数据
        # 生成对象
        tree = etree.HTML(content)
        div_list = tree.xpath('//div[@class="fleft cd-container"]/div[2]//div[@class="panel panel20 post-item post-box"]')
        for div in div_list:
            # .代表从当前位置开始找
            # 上传作者
            author = div.xpath('.//div[@class="post-author"]/a/text()')[0]
            # 标题
            title = div.xpath('.//div[@class="item-detail"]/h2[@class="item-title"]/a/text()')[0]
            # 内容
            cont = div.xpath('.//div[@class="item-detail"]/div[@class="item-content"]')
            handle_content = cont[0].xpath('string(.)').replace('\n', '').replace('\t', '')
            # 点赞数
            like_number = div.xpath('.//div[@class="item-toolbar"]/ul/li[1]/a/text()')[0]
            # 点灭数
            dont_like_number = div.xpath('.//div[@class="item-toolbar"]/ul/li[2]/a/text()')[0]

            # 将数据放到字典中
            items = {
                '作者': author,
                '标题': title,
                '内容': handle_content,
                '点赞数': like_number,
                '点灭数': dont_like_number,
            }
            # 存放到列表中
            self.items.append(items)

    # 开始爬取数据
    def run(self):
        for page in range(self.start_page, self.end_page + 1):
            print("开始读取第%s页" % page)
            request = self.handle_request(page)
            content = urllib.request.urlopen(request).read().decode()
            self.parse_content(content)
            print("结束读取第%s页" % page)
            time.sleep(2)
            string = json.dumps(self.items, ensure_ascii=False)
            with open('段子.txt', 'w', encoding="utf-8") as f:
                # f.write(str(self.items))
                f.write(string)

def main():
    start_page = int(input("请输入开始页码："))
    end_page = int(input("请输入结束页码："))

    # 创建对象，启动爬取程序
    spider = DuanZi(start_page, end_page)
    spider.run()

if __name__ == '__main__':
    main()