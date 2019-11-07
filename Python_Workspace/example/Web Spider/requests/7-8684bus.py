# -*- coding:utf-8 -*-
# time:2019/03/08 19:10
import datetime
import requests
from lxml import etree

start = datetime.datetime.now()

# 爬取公交信息
# 列表用来保存所有公交信息
items = []
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
}

def parse_navigation(): # 爬取导航链接
    url = "https://guangzhou.8684.cn/"
    r = requests.get(url, headers)
    # 解析内容，获取所有的导航链接
    tree = etree.HTML(r.text)
    # 查找以数字开头的链接
    number_href_list = tree.xpath('//div[@class="bus_kt_r1"]//a/@href')
    # 查找以字母开头的链接
    char_href_list = tree.xpath('//div[@class="bus_kt_r2"]//a/@href')
    # 将所有链接返回
    return number_href_list + char_href_list

def parse_erji_route(content):
    tree = etree.HTML(content)
    route_list = tree.xpath('//div[@class="stie_list"]//a/@href')
    route_name = tree.xpath('//div[@class="stie_list"]//a/text()')
    i = 0
    # 遍历列表
    for route in route_list:
        print("开始爬取%s线路" % route_name[i])
        route = 'https://guangzhou.8684.cn' + route
        r = requests.get(route, headers)
        # 解析内容，获取每一路公交的详细信息
        parse_sanji_route(r.text)
        print("结束爬取%s线路" % route_name[i])
        i += 1

def parse_sanji_route(content):
    tree = etree.HTML(content)
    # 依次获取内容
    # 公交线路
    bus_number = tree.xpath('//div[@class="bus_i_t1"]/h1/text()')[0]
    # 运行时间
    run_time = tree.xpath('//p[@class="bus_i_t4"][1]/text()')[0]
    # 票价信息
    ticket_info = tree.xpath('//p[@class="bus_i_t4"][2]/text()')[0]
    # 更新时间
    gxsj = tree.xpath('//p[@class="bus_i_t4"][4]/text()')[0]
    total_list = tree.xpath('//span[@class="bus_line_no "]/text()')
    # 获取上行总站数
    up_total = total_list[0]
    # 获取上行所有站名
    up_site_list = tree.xpath('//div[@class="bus_line_site "][1]/div/div/a/text()')
    try:
        # 获取下行所有站名
        down_site_list = tree.xpath('//div[@class="bus_line_site "][2]/div/div/a/text()')
        # 获取下行总站数
        down_total = total_list[1]
    except:
        down_site_list = ''
        down_total = 0
    # 将每一条公交线路信息放入字典中
    item = {
        '线路名': bus_number,
        '运行时间': run_time,
        '票价信息': ticket_info,
        '更新时间': gxsj,
        '上行站数': up_total,
        '上行站名': up_site_list,
        '下行站数': down_total,
        '下行站名': down_site_list,
    }
    items.append(item)

def parse_erji(navi_list):
    # 遍历列表，依次发送请求，解析内容，获取每一个页面所有的公交路线url
    # print(navi_list)
    for first_url in navi_list:
        first_url = 'https://guangzhou.8684.cn' + first_url
        print("开始爬取%s所有的公交信息" % first_url)
        r = requests.get(first_url, headers)
        # 解析内容，获取每一路公交的详细的url
        parse_erji_route(r.text)
        print("结束爬取%s所有的公交信息" % first_url)
def main():
    # 爬取第一页所有的导航链接（以数字或字母开头），返回列表（元素全是url）
    navi_list = parse_navigation()
    # 爬取所有公交车号（如：1路车，B1路车）
    parse_erji(navi_list)
    # 爬取完毕
    f = open("公交信息.txt", 'w', encoding="utf8")
    for item in items:
        f.write(str(item) + '\n')
    f.close()

if __name__ == '__main__':
    main()


end = datetime.datetime.now()
print("[ Finished in", (end - start), "]")