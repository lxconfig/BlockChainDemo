# -*- coding:utf-8 -*-
# time:2018/12/13 18:24

import urllib.parse

# url = 'http://www.baidu.com?name=狗蛋&pwd=123456'  #含中文字符，故为非法url
# u = urllib.parse.quote(url)
# v = urllib.parse.unquote(u)
# print(v)

url = "http://www.baidu.com/index.html"
data = {'name' : '狗蛋',
'age' : 18,
'sex' : 'm',
'height' : 180
}
#手动用字典拼接一个带有参数的url
# list1 = []
# for key, values in data.items():  #遍历字典
#     list1.append(key + '=' + str(values))
# parameters = '&'.join(list1) #将&插入到list1中
# url = url + "?" + parameters
# print(url)

#利用函数拼接
url = urllib.parse.urlencode(data) #相当于上面join步骤
print(url)
