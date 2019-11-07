# -*- coding:utf-8 -*-
# time: 2019/03/12 16:37
# File: 8-VerificationCode.py
import datetime
import requests
from lxml import etree
import urllib.request

start = datetime.datetime.now()
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
}
def download_code(url, s):
    r = s.get(url, headers=headers)
    tree = etree.HTML(r.text)
    image_src = "https://so.gushiwen.org" + tree.xpath('//img[@id="imgCode"]/@src')[0]
    # 获取表单令牌
    __VIEWSTATE = tree.xpath('//input[@name="__VIEWSTATE"]/@value')[0]
    __VIEWSTATEGENERATOR = tree.xpath('//input[@name="__VIEWSTATEGENERATOR"]/@value')[0]
    # print(image_src)
    # urllib.request.urlretrieve(image_src, 'code.png')
    # 验证码的url往往带着cookie，所以要用Session来发送请求
    r = s.get(image_src, headers=headers)
    with open("code.png", 'wb') as f:
        f.write(r.content)
    return __VIEWSTATE, __VIEWSTATEGENERATOR

def login(url, __VIEWSTATE, __VIEWSTATEGENERATOR, s):
    code = input("请输入验证码：")
    form_data = {
        '__VIEWSTATE': __VIEWSTATE,
        '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
        'from': '',
        'email': '525868229@qq.com',
        'pwd': 'shisan.com$',
        'code': code,
        'denglu': '登录',
    }
    r = s.post(url, headers=headers, data=form_data)
    with open('诗歌.html', 'w', encoding="utf8") as f:
        f.write(r.text)

def main():
    s = requests.Session()
    url = "https://so.gushiwen.org/user/login.aspx"
    # 下载验证码图片
    (__VIEWSTATE, __VIEWSTATEGENERATOR) = download_code(url, s)
    # 登录网站
    login(url, __VIEWSTATE, __VIEWSTATEGENERATOR, s)





if __name__ == '__main__':
    main()
end = datetime.datetime.now()
print("[ Finished in", (end - start), "]")