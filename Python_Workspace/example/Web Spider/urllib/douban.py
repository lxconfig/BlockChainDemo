# -*- coding:utf-8 -*-
# time:2019/02/25 20:59

import urllib.request
import urllib.parse
import os
import re


class DouBan_Movie:
    # 初始化变量
    def __init__(self, url, start_page, end_page):
        self.url = url
        self.start_page = start_page
        self.end_page = end_page

    # 拼接url，发送请求
    def handle_request(self, page):
        data = {
            'start': (page - 1) * 25,
            'filter': ''
        }
        url = self.url + urllib.parse.urlencode(data)
        request = urllib.request.Request(url)
        return request

    # 解析响应内容
    def parse_response(self, response):
        # TODO 解析内容，用正则，BS4，xpath实现内容的解析
        # 正则
        pattern_1 = re.compile(r'<div class="hd">.*?<span class="title">(.*?)</span>.*?</div>', re.S)
        pattern_2 = re.compile(r'<div class="star">.*?<span class="rating_num">(.*?)</span>.*?</div>', re.S)
        movie_title = pattern_1.findall(response)
        movie_score = pattern_2.findall(response)
        print(movie_score)
        print(len(movie_score))
        # print(movie_title)
        # print(len(movie_title))

    # 爬取程序
    def run(self):
        for page in range(self.start_page, self.end_page + 1):
            request = self.handle_request(page)
            # 获取响应
            response = urllib.request.urlopen(request).read().decode()
            # print(response)
            # 解析响应内容
            self.parse_response(response)


def main():
    url = "https://movie.douban.com/top250?"
    # https://movie.douban.com/top250?start=25&filter=unwatched，start=25表示一页的电影数
    start_page = int(input("请输入开始页码："))
    end_page = int(input("请输入结束页码："))
    # 创建类对象，调用run()方法，启动爬取程序
    spider = DouBan_Movie(url, start_page, end_page)
    spider.run()


if __name__ == "__main__":
    main()