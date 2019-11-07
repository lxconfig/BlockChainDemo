# -*- coding:utf-8 -*-
# time:2018/12/14 19:19
import urllib.request
import urllib.parse

#抓取豆瓣电影ajax
url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&"

#start是电影标号，从0开始，start=(page-1)*limit，都是偶数，limit是每页的电影数
page = input("请输入想要第几页数据：")
number = 20  #一页20条

#构建get参数
data = {
    'start': (int(page)-1) * number,
    'limit': number
}

#将字典转化成query_string
query_string = urllib.parse.urlencode(data)
url += query_string

#构建请求头，伪造浏览器
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}

#构建请求对象
request = urllib.request.Request(url, headers=headers)

#发送请求
response = urllib.request.urlopen(request)
print(response.read().decode())