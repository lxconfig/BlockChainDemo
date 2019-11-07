# -*- coding:utf-8 -*-
# time:2018/12/11 16:01
# import urllib.request
# response = urllib.request.urlopen("http://www.baidu.com")
# html = response.read() #二进制文件
# html = html.decode("utf-8")
# print(html)

# import urllib.request
# response = urllib.request.urlopen("http://placekitten.com/300/300")
# cat_img = response.read()
# with open("cat_img.jpg", 'wb') as f:
#     f.write(cat_img)

#HTTPResponse对象的status属性
# import urllib.request
# response = urllib.request.urlopen("https://www.baidu.com")
# print(response.status)

#data参数的例子
import urllib.request
import urllib.parse

data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding = 'utf-8')
response = urllib.request.urlopen("http://httpbin.org/post", data)
print(response.read())