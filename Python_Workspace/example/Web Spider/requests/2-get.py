# -*- coding:utf-8 -*-
# time:2019/03/07 15:27
import datetime
import requests

start = datetime.datetime.now()

'''
url = 'http://www.baidu.com/'
# 添加头部
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
# 发送get请求
r = requests.get(url, headers=headers) # r是一个响应对象
# r.encoding = 'utf8' # r.encoding可以查看网页编码，也可以赋值改变网页编码
print(r.text)  # r.text可以查看网页响应内容
'''

# 带参数的get
url = "https://www.baidu.com/s"
data = {
    'ie': 'utf-8',
    'wd': '中国',
}
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
r = requests.get(url, headers=headers, params=data)
# print(r.status_code)
# print(r.headers)

# 写入文件中
with open('baidu.html', 'wb') as f:
    f.write(r.content) # 字节类型
    # f.write(r.text)  # 字符串类型

end = datetime.datetime.now()
print("[ Finished in", (end - start), "]")