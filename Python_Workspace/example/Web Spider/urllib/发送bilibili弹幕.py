# -*- coding:utf-8 -*-
# time:2018/12/21 16:00
import urllib.request
import urllib.parse

keyword = input("输入弹幕：")
url = "https://api.live.bilibili.com/msg/send"
form_data = {
    'color': '16777215',
    'fontsize': '25',
    'mode': '1',
    'msg': keyword,
    'rnd': '1545379087',
    'roomid': '3683436',
    'csrf_token': 'ce3d17f240b922ab1190108d7fe3e0a3',
    'csrf': 'ce3d17f240b922ab1190108d7fe3e0a3',
}
form_data = urllib.parse.urlencode(form_data).encode()

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'LIVE_BUVID=AUTO7715339683947990; sid=4j63hybl; fts=1533968445; '
              'buvid3=DEC6C65F-3701-40B4-8407-5E06E478342827970infoc; rpdid=oxqsloqskldoskklxqpxw; '
              'UM_distinctid=16527b06b3918-0256970c0311c8-37664109-1fa400-16527b06b3a1fb; stardustvideo=1; '
              'im_notify_type_577850=0; CURRENT_FNVAL=16; DedeUserID=577850; DedeUserID__ckMd5=628f716f2acb3618; '
              'SESSDATA=08e79749%2C1547607673%2Cd8e62ac1; bili_jct=ece831e018cd7bbc55f8fe4c33690285; CURRENT_QUALITY=80;'
              ' bp_t_offset_577850=199095979261716194; finger=17c9e5f5; _dfcaptcha=df0493bed9cdbf602aa119fb92d3d8cc; '
              'Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1544594714,1544594718,1545379072; '
              'Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1545379090',
    'Host': 'api.live.bilibili.com',
    'Origin': 'https://live.bilibili.com',
    'Pragma': 'no-cache',
    'Referer': 'https://live.bilibili.com/3683436?visit_id=flj4xtx2ty0',
}

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request, form_data)
print(response.read().decode())