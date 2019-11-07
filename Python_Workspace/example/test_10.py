# -*- coding:utf-8 -*-
# time:2018/12/12 15:36

#timeout参数的例子
import urllib.request
response = urllib.request.urlopen("http://www.google.com", timeout=1)
print(response.read())
