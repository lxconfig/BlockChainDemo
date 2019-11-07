# -*- coding:utf-8 -*-
# time:2018/12/17 20:01
import urllib.request
import urllib.parse
import os.path

url = "http://tieba.baidu.com/f?ie=utf-8&"
name = input("请输入吧名：")
start_page = int(input("请输入起始页："))
end_page = int(input("请输入结束页："))

#创建文件夹
dir_name = name + '_1'
if not os.path.exists(dir_name):
     os.mkdir(dir_name)
#循环依次爬取每一页数据，page表示当前页
for page in range(start_page, end_page + 1):
    #构建get参数
    data = {
        'kw': name,
        'pn': (page - 1) * 50,
    }
    #构建完整的url
    query_sting = urllib.parse.urlencode(data)
    url_t = url + query_sting

    #构建请求头，伪装浏览器访问
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        # 'Accept': '*/*',
        # 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        # 'Cache-Control': 'no-cache',
        # 'Connection': 'keep-alive',
        # 'Cookie': 'PSTM=1533956227; BIDUPSID=FF51A737B73C48CA0AD9EA12109688BD; BAIDUID=92026B575C968B971C0AAFE0B84A5B37:FG=1;TIEBA_USERTYPE=c061bb2c97a43a9875c43d1b; bdshare_firstime=1533971004183; MCITY=-%3A; BDUSS=Rlfmt1Zm1CSmlMeTRRMGlPa0k0NGpxN0tkU2V2alZ0RkdlVktNNXRTeXA4LUpiQUFBQUFBJCQAAAAAAAAAAAEAAAB0igQiODLE6rXEt~DX5gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKlmu1upZrtbaW; TIEBAUID=f6f1ec33d56a284a8929cf42; BDRCVFR[nnelRoIzZZm]=mk3SLVN4HKm; delPer=0; PSINO=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BCLID=6730160493502202773; BDSFRCVID=XA_OJeC62xMKMa39QkZ5baprfg5Ib3oTH6aIA71F3nb6q4kELtQZEG0Ptf8g0Ku-f-9-ogKK3gOTH4DF_2uxOjjg8UtVJeC6EG0P3J; H_BDCLCKID_SF=tbIj_CPatCvbfP0kj502e5vXDNAHJK62aKDX3buQypjr8pcNLTDK2MuUXfLeqloWyJTa34J-5J0hOJ_RhpO1j4_PLHtD0jJXKJcD_nvNBPbGol5jDh3Mb6ksD-Rte4KLf4jy0hvctb3cShPmQMjrDRLbXU6BK5vPbNcZ0l8K3l02VKO_e4bK-TrLjHutJx5; H_PS_PSSID=1465_21089_18560_20692_28131_27751_27245_22158; STOKEN=469904f87f7199fe64d151f085466e29933f5fc3b3a3858cfa931f985f1f2360; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1544014830,1544506571,1544601102,1545047707; 570722932_FRSVideoUploadTip=1; wise_device=0; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1545048341',
        # 'Host': 'tieba.baidu.com',
        # 'Pragma': 'no-cache',
        # 'Referer': 'http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=0',
        # 'X-Requested-With': 'XMLHttpRequest',
    }

    #构建请求对象
    request = urllib.request.Request(url_t, headers=headers)
    print("第%d页开始下载......" % page)

    #发送请求
    response = urllib.request.urlopen(request)

    #创建文件名,将工作空间移到创建的文件夹dir_name下
    file_name = name + '_' + str(page) + '.html'
    path = dir_name + '\\' + file_name

    with open(path, 'w', encoding="utf-8") as f:
        f.write(response.read().decode())
    print("第%d页结束下载......" % page)