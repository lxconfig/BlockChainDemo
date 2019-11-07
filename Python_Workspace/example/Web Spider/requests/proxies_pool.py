# -*- coding:utf-8 -*-
# time: 2019/04/22 19:04
# File: proxies_pool.py
import requests
import random
from lxml import etree
'''
1.爬取代理数据：ip+port（西刺代理）
2.验证代理是否可行：向百度发送get请求，查看状态码
3.记录可行的代理：记录到txt中
'''

# 爬取代理数据  https://www.xicidaili.com/nn/
def Spider_proxy(start_url, page):
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    ]
    user_agent = random.choice(user_agent_list)
    headers = {
        'User-Agent': user_agent
    }
    response = requests.get(start_url, headers= headers)
    # 解析响应内容（xpath）
    tree = etree.HTML(response.text)
    tr_list = tree.xpath('//table[@id="ip_list"]//tr[position()>1]')
    # next_url = tree.xpath('//a[@class="next_page"]/@href')[0]
    # next_url = "https://www.xicidaili.com" + next_url
    for tr in tr_list:
        ip_list = tr.xpath('./td[2]/text()')
        port_list = tr.xpath('./td[3]/text()')
        kind = tr.xpath('./td[6]/text()')
        proxy = [kind[i] + "://" + ip_list[i] + ":" + port_list[i] for i in range(0, len(ip_list))][0]
        is_available = CheckProxy(proxy, headers)
        if is_available:
            with open("proxy.txt", "a+", encoding="utf-8") as f:
                f.write(proxy + '\n')
    # Spider_proxy(next_url)

# 验证代理是否可用
def CheckProxy(proxy, headers):
    target_url = "https://www.baidu.com"
    proxies = {"http": proxy, "https": proxy}
    # response = requests.get(target_url, headers=headers, proxies=proxies,).status_code
    # print(response)
    try:
        response = requests.get(target_url, headers= headers, proxies=proxies, timeout=10).status_code
        if response == 200:
            return True
        else:
            return False
    except:
        return False

def main():
    start_page = int(input("请输入开始爬取的页数："))
    end_page = int(input("请输入结束爬取的页数："))
    for page in range(start_page, end_page + 1):
        start_url = "https://www.xicidaili.com/nn/{}".format(page)
        Spider_proxy(start_url, page)

if __name__ == '__main__':
    main()