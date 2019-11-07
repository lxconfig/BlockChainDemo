# -*- coding:utf-8 -*-
# time:2019/03/10 14:54
import datetime
import requests
from lxml import etree

start = datetime.datetime.now()

def send_requests(url):
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    }
    r = requests.get(url, headers=headers)
    # print(r.text)
    return r.text

def parse_site_info(content):
    tree = etree.HTML(content)
    # 公交线路信息
    bus_info = tree.xpath('//div[@class="bus_i_content"]//text()')
    bus_info[0] = bus_info[0].replace('&nbsp', '')
    # 上行总站数
    up_siteTotal = tree.xpath('//div[@class="bus_line_top "][1]/span/text()')[0]
    up_siteTotal = up_siteTotal.replace('\xa0', '')
    # print(up_siteTotal)
    # 上行站台信息
    up_site_info = tree.xpath('//div[@class="bus_line_site "][1]/div/div/a/text()')
    try:
        # 下行总站数
        down_siteTotal = tree.xpath('//div[@class="bus_line_top "][2]/span/text()')[0]
        down_siteTotal = down_siteTotal.replace('\xa0', '')
        # 下行站台信息
        down_site_info = tree.xpath('//div[@class="bus_line_site "][2]/div/div/a/text()')
    except:
        down_siteTotal = 0
        down_site_info = ''
    # 将信息放入字典中
    item = []
    dict_info = {
        '公交线路信息': bus_info,
        '上行总站数': up_siteTotal,
        '上行站台信息': up_site_info,
        '下行总站数': down_siteTotal,
        '下行站台信息': down_site_info,
    }
    # print(dict_info)
    item.append(dict_info)
    # print(item)
    for i in item:
        with open("bus_info.txt", 'a') as f:
            f.write(str(i) + '\n')

def parse_route(content):
    tree = etree.HTML(content)
    bus_link = tree.xpath('//div[@id="con_site_1"]/a/@href') # 获取每路车信息页面的url
    bus_name = tree.xpath('//div[@id="con_site_1"]/a/text()') # 获取每路车的名字
    # print(bus_link)
    # print(len(bus_link))
    i = 0
    for link in bus_link:
        url = "https://ganzhou.8684.cn" + str(link)
        content = send_requests(url)
        # print(content)
        # exit()
        # 获取每一路公交的详细信息,并存入excel中
        print("开始爬取%s路车的信息" % bus_name[i])
        parse_site_info(content)
        print("结束爬取%s路车的信息" % bus_name[i])
        i += 1

def parse_kt(content):
    tree = etree.HTML(content)
    number_kt_link = tree.xpath('//div[@class="bus_kt_r1"]/a/@href') # 数字开头
    char_kt_link = tree.xpath('//div[@class="bus_kt_r2"]/a/@href') # 字母开头
    kt_link = number_kt_link + char_kt_link
    for link in kt_link:
        url = "https://ganzhou.8684.cn" + str(link)
        # print(url)
        # 发送请求，返回以x开头所有车次的html
        content = send_requests(url)
        # print(content)
        # exit()
        # 获取每路车的url
        parse_route(content)

def main():
    url = "https://ganzhou.8684.cn/"
    # 发送请求，返回响应内容
    content = send_requests(url)
    # 获取公交路线开头信息
    parse_kt(content)

if __name__ == '__main__':
    main()
end = datetime.datetime.now()
print("[ Finished in", (end - start), "]")