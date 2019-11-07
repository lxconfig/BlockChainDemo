# -*- coding:utf-8 -*-
# time:2019/02/28 15:06

import urllib.request
import urllib.parse
import http.cookiejar


# 创建cookiejar实例
cookie = http.cookiejar.CookieJar()
# 创建cookie的管理器
handler = urllib.request.HTTPCookieProcessor(cookie)
# 创建opener
opener = urllib.request.build_opener(handler)

def login():
    url = "https://login.taobao.com"
    TPL_username = input("请输入用户名：")
    TPL_password = input("请输入密码：")
    data = {
        "TPL_username": TPL_username,
        "TPL_password": TPL_password,
        'ncoSig': 'e572199c5eaa8e6c87c4420092bc1871f19cbe31', 'ncoSessionid': 'false', 'ncoToken': 'false',
        'slideCodeShow': 'zh_CN', 'useMobile': '0', 'lang': '', 'loginsite': 'https://www.taobao.com/',
        'newlogin': 'tb', 'TPL_redirect_url': 'default', 'from': 'default', 'fc': '', 'style': 'false',
        'css_style': 'true', 'keyLogin': 'false', 'qrLogin': 'false', 'newMini': '3', 'newMini2': '', 'tid': '',
        'loginType': '', 'minititle': '', 'minipara': '', 'pstrong': '', 'sign': '', 'need_sign': '', 'isIgnore': '',
        'full_redirect': ''
    }
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        'Connection': 'keep-alive',
    }
    data = urllib.parse.urlencode(data).encode()
    request = urllib.request.Request(url, data=data, headers=headers)
    response = opener.open(request)
    # print(response.read().decode("gbk"))
    # with open("淘宝1.html", 'w', encoding="gbk") as f:
    #     f.write(response.read().decode("gbk"))

def GetHomePage():
    url = "https://rate.taobao.com/feedRateList.htm?auctionNumId=561281944948&userNumId=40400717&currentPageNum=1&pageSize=20"
    # response = opener.open(url)
    # with open("淘宝2.html", 'w', encoding="utf8") as f:
    #     f.write(response.read().decode())
    response = opener.open(url)
    print(response.read().decode())


if __name__ == '__main__':
    login()
    GetHomePage()