# -*- coding:utf-8 -*-
# time:2018/12/14 19:55
import urllib.request
import urllib.parse

url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"
city = input("请输入城市：")
page = input("请输入要查询第几页：")
size = input("请输入要多少个：")

# #构建get参数
# get_data = {
#     "op": cname
# }
#
# #处理get参数，构成完整url
# query_string = urllib.parse.urlencode(get_data)
# url += query_string

#构建form参数,并处理
form_data = {
    'cname': city,
    'pageIndex': page,
    'pageSize': size,
}
form_data = urllib.parse.urlencode(form_data).encode()

#构建请求头，伪装浏览器
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}

#构建请求对象
request = urllib.request.Request(url, headers=headers)

#发送请求
response = urllib.request.urlopen(url, form_data)
print(response.read().decode())