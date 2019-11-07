# -*- coding:utf-8 -*-
# time:2018/12/13 19:54

import urllib.request
import urllib.parse

url = 'http://www.baidu.com/'  #使用fiddler抓包时，url最后要加/，否则报错

#要伪装的头部，构建UA
headers = {'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
#构建请求对象
request = urllib.request.Request(url=url, headers=headers)

#发送请求
response = urllib.request.urlopen(request)
print(response.read().decode())