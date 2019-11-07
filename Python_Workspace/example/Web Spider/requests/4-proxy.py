# -*- coding:utf-8 -*-
# time:2019/03/07 20:56
import datetime
import requests

start = datetime.datetime.now()

url = "http://www.baidu.com/s?ie=UTF-8&wd=ip"
proxies = {
    'http': 'http://122.41.171.223:4684'
}
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
}
r = requests.get(url, headers=headers, proxies=proxies)
with open('daili.html', 'wb') as f:
    f.write(r.content)







end = datetime.datetime.now()
print("[ Finished in", (end - start), "]")