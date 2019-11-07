# -*- coding:utf-8 -*-
# time: 2019/03/14 20:39
# File: 10-download_video.py
import datetime
import requests
import jsonpath
import json
from selenium import webdriver
from lxml import etree
import time
start = datetime.datetime.now()
'''
url = "http://v3-tt.ixigua.com/ecf304675145671f10376053ad0ab851/5c8a5f53/video/m/" \
      "2209ccdf94b21314b798c984a1a26cd05f211618a30700006867b17400e9/?rc=Mzp4cjQ6aWpsbDMzZzczM0ApQHRAbzg2NTc5MzQzMzg3N" \
      "TQzNDVvQGgzdSlAZjN1KWRzcmd5a3VyZ3lybHh3Zjc2QGlkZm00YzQ2L18tLWEtL3NzLW8jbyM2MDQuLjItLjE1LTEwNi06I28jOmEtcSM6YHZpXG" \
      "JmK2BeYmYrXnFsOiMzLl4%3D&vfrom=xgplayer"
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
}
r = requests.get(url, headers=headers)
# 视频用二进制文件存取
with open('1.mp4', 'wb') as f:
    f.write(r.content)
'''
# 下载365yg网站上的视频
class Spider:
    def __init__(self, url):
        self.url = url
    def send_request(self, url):
        headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        }
        r = requests.get(url=url, headers=headers)
        return r.text

    def phantom(self, a_src):
        browser = webdriver.PhantomJS(r'E:\Python37\example\Web Spider\phantomjs-2.1.1-windows\bin\phantomjs.exe')
        browser.get(a_src)
        time.sleep(10)
        with open("2.html", 'w', encoding="utf8") as f:
            f.write(browser.page_source)
        exit()
        browser.close()
        # 获取源码，生成tree对象，然后查找video的src属性
        # tree = etree.HTML(browser.page_source)
        # video_src = tree.xpath("//video/@src")
        # print(video_src)

    def parse_content(self, content):
        obj = json.loads(content)
        video_title = jsonpath.jsonpath(obj, '$..title')
        source_src = jsonpath.jsonpath(obj, '$..source_url')
        for src in source_src:
            a_src = "http://www.365yg.com" + src
            # 用phantomjs来解决
            self.phantom(a_src)

    # 开始爬取
    def run(self):
        content = self.send_request(self.url)
        self.parse_content(content)


def main():
    url = "http://365yg.com/api/pc/feed/?max_behot_time=1552650228&category=video_new&utm_source=toutiao&widen=3&tadrequire=true&as=A1B50C483BF93BC&cp=5C8BB9934B2C2E1&_signature=aqpAfhAZNiXAhQD-gPX1vmqqQG"
    spider = Spider(url)
    spider.run()

if __name__ == '__main__':
    main()
end = datetime.datetime.now()
print("[ Finished in", (end - start), "]")