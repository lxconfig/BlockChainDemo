# -*- coding:utf-8 -*-
# time:2019/02/25 21:10

# from lxml import etree
#
# tree = etree.parse("book.json")
# content = tree.xpath('/store/book/author')
# print(content)

import urllib.request
import urllib.parse
import http.cookiejar
from lxml import etree
import requests
import re

# 抓包，复制cookie，爬取登录后的网页
'''
url = "http://www.renren.com/889370168/profile"
headers = {
    'cookie': 'anonymid=jput3htlh8juua; _r01_=1; depovince=GUZ; ln_uact=525868229@qq.com; ln_hurl=http://head.xiaonei.com/photos/0/0/women_main.gif; jebe_key=1148a331-e8aa-40d9-b4b7-4bcef88dc48d%7C5fee311c92f55a9f7c6313f7fca1377a%7C1551361450261%7C1%7C1551361449683; wp=0; JSESSIONID=abcc-g_Xhx-5cdBicL3Kw; ick_login=283ef4f3-b51e-4523-8c3f-5e5c1ce20cb9; first_login_flag=1; wp_fold=0; jebecookies=8581d171-8a19-4c6b-ba1f-2ea2e1c918b5|||||; _de=B192BF27B05F9FB0E2A69D838E8B6F33696BF75400CE19CC; p=012759300048285cc6ab3f61794040518; t=92ea8e1601319bcdbfd0ff42415e71658; societyguester=92ea8e1601319bcdbfd0ff42415e71658; id=889370168; xnsid=c84d3d8d; ver=7.0; loginfrom=null',
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
}
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request).read().decode()
with open('练习.html', 'w', encoding="utf8") as f:
    f.write(response)
'''

'''
# 利用cookiejar，自动使用cookie

# 创建cookiejar对象,cookie就存放在其中
cookie = http.cookiejar.CookieJar()
# 创建常见cookie的管理器
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)
# 创建请求管理器opener
opener = urllib.request.build_opener(cookie_handler)

def login():
    # 负责首次登陆记录用户cookie
    url = "http://www.renren.com/PLogin.do"
    email = input("请输入用户名：")
    password = input("请输入密码：")
    data = {
        'email': email,
        'password': password
    }
    headers = {
        'Referer': 'https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4006-17288034551.33.13402c5aZ3I3E1&id=583939478446&scene=taobao_shop&sku_properties=5919063:6536025',
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    }
    # 把data编码
    data = urllib.parse.urlencode(data).encode()
    # 构建请求对象
    request = urllib.request.Request(url, data=data, headers=headers)
    # 用opener发送请求,cookie保存在opener中
    response = opener.open(request)
    print(response.read().decode())

def GetHomePage():
    # 爬取个人主页
    url = "http://www.renren.com/889370168/profile"
    request = opener.open(url).read().decode()
    with open("练习.html", 'w', encoding="utf8") as f:
        f.write(request)

if __name__ == '__main__':
    login()
    GetHomePage()
'''

'''
url = "https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fwww.taobao.com%2F"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request).read().decode("gbk")
# print(response)

tree = etree.HTML(response)
name_list = tree.xpath("//div[@class='submit']//input[@type='hidden']/@name")[:26]

value_list = tree.xpath("////div[@class='submit']//input[@type='hidden']/@value")[:26]

dict1 = dict(zip(name_list, value_list))
print(dict1)
'''

# 抓取西刺代理网站的ip信息
start_page = int(input("请输入开始页码："))
end_page = int(input("请输入结束页码："))

url = "https://www.xicidaili.com/wn/"
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    'Cookie': '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWUxNWFmNWNiN2JjM2ZhZWIyNGRjNzc0ZWRmOGFiNzVhBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMU5OSmhmNjBVcDRZZ2FmNVgxV3lRNU8yeGZxN2E4L3pqTXA1RkpJTFN4bkE9BjsARg%3D%3D--e5761cd4c496e354e9d8c1d09610c77a1531b715; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1551959087; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1551959473',
}
# request = urllib.request.Request(url, headers=headers)
# response = urllib.request.urlopen(request).read().decode()
# print(response)
for page in range(start_page, end_page + 1):
    get_url = url + str(page)

    r = requests.get(get_url, headers=headers)
    tree = etree.HTML(r.text)
    address = tree.xpath(r'//table[@id="ip_list"]//tr/td[2]/text()')
    port = tree.xpath(r'//table[@id="ip_list"]//tr/td[3]/text()')

    # 将ip和端口拼接起来
    for i in range(0, len(address)):
        ip = address[i] + ':' + port[i] + '\n'
        print(ip)
        with open("proxy.txt", 'a+') as f:
            f.write(ip)