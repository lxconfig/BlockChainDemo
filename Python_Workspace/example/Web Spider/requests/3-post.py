# -*- coding:utf-8 -*-
# time:2019/03/07 16:43
import datetime
import requests
import json

start = datetime.datetime.now()
keyword = input("请输入文本：")
url = "https://cn.bing.com/ttranslate?&category=&IG=94209012FDE64AF8A5453B71939604EA&IID=translator.5038.7"
form_data = {
    'text': keyword,
    'from': 'en',
    'to': 'zh-CHS',
}
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
r = requests.post(url=url, headers=headers, data=form_data)
t = json.loads(r.text)
print("%s的意思是：%s" % (keyword, t['translationResponse']))


end = datetime.datetime.now()
print("[ Finished in", (end - start), "]")