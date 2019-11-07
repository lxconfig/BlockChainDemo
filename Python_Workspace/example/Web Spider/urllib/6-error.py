# -*- coding:utf-8 -*-
# time:2018/12/18 14:00

import urllib.request
import urllib.parse
import urllib.error

#URLError
# url = "http://www.maodan.com/"
# try:
#     response = urllib.request.urlopen(url)
#     print(response)
# # except Exception as e:   #Exception是所有错误类的基类
# #     print(e)
# except urllib.error.URLError as e:
#     print(e)

#HTTPError
url = "https://blog.csdn.net/zcf1784266476/article/details/7133594"  #错误的域名
try:
    response = urllib.request.urlopen(url)
    print(response)
except urllib.error.HTTPError as e:  #HTTPError是URLError的子类，先捕获子类，在捕获父类
    print(e)
except urllib.error.URLError as e:
    print(e)