# -*- coding:utf-8 -*-
# time:2018/12/18 15:07
import urllib.request
import urllib.parse

#创建handler,配置代理
handler = urllib.request.ProxyHandler({'http': '114.215.95.188:3128'})

#创建opener
opener = urllib.request.build_opener(handler)

url = 'http://www.baidu.com/s?ie=UTF-8&wd=ip'
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
}

request = urllib.request.Request(url, headers=headers)
response = opener.open(request)
with open('ip.html', 'wb') as f:
    f.write(response.read())