# -*- coding:utf-8 -*-
# time:2018/12/14 15:52
import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/v2transapi'
keyword = input("请输入要翻译的单词或者句子：")

#构建表单数据
form_data = {
'from':'en',
'query':keyword,
'sign':'198772.518981',  #js加密，所以无法爬取，每个单词都对应着一个sign
'simple_means_flag':'3',
'to':'zh',
'token':'648fbc72aacbe0f194fb6ba9b86eb6c9',
'transtype':'realtime',
}

#处理表单数据
form_data = urllib.parse.urlencode(form_data).encode()

#构建请求头，伪装浏览器
data = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
'Host': 'fanyi.baidu.com',
'Connection': 'keep-alive',
#'Content-Length': 121,
'Accept': '*/*',
'Origin': 'https://fanyi.baidu.com',
'X-Requested-With': 'XMLHttpRequest',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Referer': 'https://fanyi.baidu.com/',
#'Accept-Encoding': 'gzip, deflate, br',  #声明浏览器支持的编码类型
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
'Cookie': 'PSTM=1533956227; BIDUPSID=FF51A737B73C48CA0AD9EA12109688BD; BAIDUID=92026B575C968B971C0AAFE0B84A5B37:FG=1; MCITY=-%3A; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=Rlfmt1Zm1CSmlMeTRRMGlPa0k0NGpxN0tkU2V2alZ0RkdlVktNNXRTeXA4LUpiQUFBQUFBJCQAAAAAAAAAAAEAAAB0igQiODLE6rXEt~DX5gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKlmu1upZrtbaW; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22it%22%2C%22text%22%3A%22%u610F%u5927%u5229%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; pgv_pvi=3475392512; H_PS_PSSID=1465_21089_18560_20692_27751_27245_22158; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1543975898,1544255858,1544518360,1544769181; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1544772291'
}

#构建请求
request = urllib.request.Request(url, headers=data)

#发送请求
response = urllib.request.urlopen(request, form_data)
html = response.read().decode()
print(html)
# h = json.loads(html)
# print(h)
# print(keyword + "：%s" % h['trans_result']['data'][0]['dst'])