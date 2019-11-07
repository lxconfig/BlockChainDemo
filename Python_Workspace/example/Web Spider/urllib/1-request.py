# -*- coding:utf-8 -*-
# time:2018/12/13 16:37
import urllib.request

url = "http://www.baidu.com"
response = urllib.request.urlopen(url)
#read()方法，读取响应内容，内容是字节类型（二进制）
# with open("baidu.html", 'w', encoding="utf-8") as f:
#     f.write(response.read().decode())

#打开方式选择wb，则不用指定编码
# with open("baidu1.html", 'wb') as f1:
#     f1.write(response.read())

#geturl()方法，获取请求的url地址
#print(response.geturl())

#getheaders()方法,返回的是响应头信息，列表+元组的形式，可以转化为dict
#print(response.getheaders())
#print(dict(response.getheaders()))

#getcode()方法，获取状态码
#print(response.getcode())

#readlines(),返回一个列表，按行读取，都是字节类型
#print(response.readlines())

#下载图片
# image_url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1544705988480&di=efe32b767b2a5dfdf628524a1562e3ff&imgtype=0&src=http%3A%2F%2Fimgsrc.baidu.com%2Fimage%2Fc0%253Dshijue1%252C0%252C0%252C294%252C40%2Fsign%3D45d1210eb91bb0519b29bb6b5e13b0c1%2Ff9198618367adab4a64b366f81d4b31c8701e407.jpg'
# response = urllib.request.urlopen(image_url)

#图片只能写入本地二进制的格式
# with open("mao.jpg", 'wb') as f:
#     f.write(response.read())

#urllib.request.urlretrieve(image_url, 'mao1.jpg')