# -*- coding:utf-8 -*-
# time:2018/12/19 15:10
import urllib.request
import urllib.parse
import http.cookiejar  #用来保存cookie

#真实的模拟浏览器，当发送完post请求的时候，将cookie保存到代码中
#创建一个cookiejar对象
cj = http.cookiejar.CookieJar()  #cookie会保存到cj中

#通过cookiejar对象创建一个handler
handler = urllib.request.HTTPCookieProcessor(cj)

#根据handler创建一个opener
opener = urllib.request.build_opener(handler)

url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=20181131510334'
form_data = {
    'email': '525868229@qq.com',
    'icode': '',
    'origURL': 'http://www.renren.com/home',
    'domain': 'renren.com',
    'key_id': '1',
    'captcha_type': 'web_login',
    'password': '6628bb581d23090d8ac7534a2d3f236205a5afa4f3e19e2332c09191c96456d6',
    'rkey': '8792c5a430e935bc4fe69f9f4c7203f9',
    'f': 'http%3A%2F%2Fwww.renren.com%2F889370168%2Fnewsfeed%2Ffocus',
}
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
}
form_data = urllib.parse.urlencode(form_data).encode()
request = urllib.request.Request(url, headers=headers)
response = opener.open(request, form_data)
print(response.read().decode())
print('*' * 50)

get_url = 'http://www.renren.com/889370168/profile'
request = urllib.request.Request(get_url, headers=headers)
response = opener.open(request)
with open('renren.html', 'w', encoding='utf-8') as f:
    f.write(response.read().decode())
