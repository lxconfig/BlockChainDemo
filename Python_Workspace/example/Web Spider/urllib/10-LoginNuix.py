# -*- coding:utf-8 -*-
# time:2019/03/04 19:37
import datetime
import urllib.request
import urllib.parse
import jsonpath
import json

start = datetime.datetime.now()

url = "http://account.chinaunix.net/login/login"
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    'Connection': 'keep-alive',
}
form_data = {
    'username': 'dweller',
    'password': 'shisan.com$',
    '_token': 'rF3kUn4tg4yz9gJkv6kfCfvyeBByxfWztsDrwFQV',
    '_t': '1551873852838',
    'Cookie': 'pgv_pvid=6281535936; XSRF-TOKEN=rF3kUn4tg4yz9gJkv6kfCfvyeBByxfWztsDrwFQV; laravel_session=NxHI1CLiPA24UEXEKKWo9kMRPFDqDSZMq3Qz91Wr; account_chinauni=accountchinauni; Hm_lvt_0ee5e8cdc4d43389b3d1bfd76e83216b=1551700844,1551771706,1551872660; __utma=225341893.928315318.1551701398.1551776732.1551872661.4; __utmc=225341893; __utmz=225341893.1551872661.4.4.utmcsr=account.chinaunix.net|utmccn=(referral)|utmcmd=referral|utmcct=/ucenter/user/index; __pts=353265800; __ptb=353265800; pgv_info=ssid=s4079895300; __pta=1282074696.1551700844.1551875264.1551875271.29; Hm_lpvt_0ee5e8cdc4d43389b3d1bfd76e83216b=1551875271; st_user_token=5a30f9f6add47741639310112b8d02de; account_user=69912230%7Cdweller%7Chttp%3A%2F%2Fimg.account.itpub.net%2Fhead%2Fuser.jpg%3Fx-oss-process%3Dstyle%2Fm; __backurl=http%3A%2F%2Fbbs.chinaunix.net%2F',
}
form_data = urllib.parse.urlencode(form_data).encode()
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request, data=form_data).read().decode()
# print(response)
with open("bbs.json", 'w', encoding="gbk") as f:
    f.write(response)

obj = json.load(open("bbs.json", 'r', encoding="gbk"))
print(obj)
ret = jsonpath.jsonpath(obj, '$.data.url')[0]
print(ret)














end = datetime.datetime.now()
print("[ Finished in", (end - start), "]")