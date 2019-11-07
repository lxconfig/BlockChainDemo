# -*- coding:utf-8 -*-
# time:2018/12/18 14:26
import urllib.request
import urllib.parse

url = 'http://www.baidu.com/'
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
}

#创建一个handler
handler = urllib.request.HTTPHandler()

#通过handler，创建一个opener
#opener就是一个对象，可以直接使用opener里面的方法发送请求，不要使用urlopen
opener = urllib.request.build_opener(handler)

#构建请求对象
request = urllib.request.Request(url, headers=headers)

#发送请求
response = opener.open()
print(response.read().decode())