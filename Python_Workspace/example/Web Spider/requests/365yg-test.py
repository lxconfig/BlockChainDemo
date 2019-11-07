# -*- coding:utf-8 -*-
# time: 2019/03/16 14:22
# File: 365yg-test.py
import datetime
import requests
import jsonpath
import json
from selenium import webdriver
import time

start = datetime.datetime.now()
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
}
def parse_href(content):
    obj = json.loads(content)
    # 每一条视频的名称
    title = jsonpath.jsonpath(obj, '$.data..title')
    # 每一条视频的地址
    a_href = jsonpath.jsonpath(obj, '$.data..source_url')
    for href in a_href:
        video_info = "http://www.365yg.com" + href
        parse_info(video_info)

def parse_info(video_info):
    # 利用Phantomjs
    browser = webdriver.PhantomJS(r'E:\Python37\example\Web Spider\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    browser.get(video_info)
    time.sleep(5)
    browser.close()

def main():
    for widen in range(1,3):
        url = "http://www.365yg.com/api/pc/feed/?min_behot_time=0&category=video_new&utm_source=toutiao&widen={}&tadrequire=true&as=A155DCD81C4978B&cp=5C8C79D7A8EB0E1&_signature=FdskERAWSVy.9GSR3HR-uhXbJA"
        url = url.format(widen)
        r = requests.get(url=url, headers=headers)
        parse_href(r.text)


if __name__ == '__main__':
    main()

end = datetime.datetime.now()
print("[ Finished in", (end - start), "]")