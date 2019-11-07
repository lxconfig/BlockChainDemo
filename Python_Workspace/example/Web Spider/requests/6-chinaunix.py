# -*- coding:utf-8 -*-
# time:2019/03/08 15:24
import datetime
import requests
from bs4 import BeautifulSoup

start = datetime.datetime.now()
s = requests.Session()
# 登录chinaunix论坛
# 访问登录页面，获取登录需要的一些参数
get_url = "http://account.chinaunix.net/login/?url=http%3A%2F%2Fbbs.chinaunix.net%2F"
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
}
r = s.get(get_url, headers=headers)
# 生成soup对象，获取隐藏值
soup = BeautifulSoup(r.text, 'lxml')
token = soup.select('input[name="_token"]')[0]['value']

# 向指定的post发送请求，完成登录
post_url = "http://account.chinaunix.net/login/login"
form_data = {
    'username': 'dweller',
    'password': 'shisan.com$',
    '_token': token,
    '_t': '1552030581626',
}
h = s.post(post_url, headers=headers, data=form_data)

# 访问登录后的页面
info_url = "http://bbs.chinaunix.net/home.php?mod=space&uid=69912230&do=profile"
n = s.get(info_url, headers=headers)
with open('info.html', 'wb') as f:
    f.write(n.content)









end = datetime.datetime.now()
print("[ Finished in", (end - start), "]")