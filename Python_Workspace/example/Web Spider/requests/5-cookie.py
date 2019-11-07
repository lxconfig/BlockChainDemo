# -*- coding:utf-8 -*-
# time:2019/03/08 14:23
import datetime
import requests

start = datetime.datetime.now()
# 用requests库实现人人网登录以及cookie
# 如果碰到会话相关的问题，要首先创建一个会话
s = requests.Session()
post_url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019251426936"
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
}
form_data = {
    'email': '525868229@qq.com',
    'icode': 'origURL	http://www.renren.com/home',
    'domain': 'renren.com',
    'key_id': '1',
    'captcha_type': 'web_login',
    'password': '134b30925da9eec411f2b96a523e9d76b5403f0e5508b73b314c097662541ed9',
    'rkey': 'b88b052e1aa66a78cdbf13188f021a5f',
    'f': 'http%3A%2F%2Fwww.renren.com%2F889370168',
}
r = s.post(post_url, headers=headers, data=form_data) # 返回true，登录成功
# print(r.text)


get_url = "http://www.renren.com/889370168/profile"
h = s.get(get_url, headers=headers)
# print(h.text)


end = datetime.datetime.now()
print("[ Finished in", (end - start), "]")