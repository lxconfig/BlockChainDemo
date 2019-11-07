# -*- coding:utf-8 -*-
# time:2018/12/13 19:27

#get方式
import urllib.request
import urllib.parse

keyword = input('请输入关键字搜索:')
file_name = keyword + '.html'
url = 'http://www.baidu.com/s'
data = {'ie':'utf-8',
        'wd':keyword
        }
parameters = urllib.parse.urlencode(data)
url = url + '?' + parameters

response = urllib.request.urlopen(url)
with open(file_name, 'w', encoding='utf-8') as f: #编码要一致，文件编码是utf-8，写入文件也要是utf-8
    f.write(response.read().decode())