# -*- coding:utf-8 -*-
# time: 2019/03/10 17:08
# File: test.py
import datetime
import requests
from lxml import etree
import csv

start = datetime.datetime.now()

# headers = {
#     'User-Agent':
#         'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
# }
# url = "https://guangzhou.8684.cn/x_005947d5"
# r = requests.get(url, headers=headers)
# content = r.text
# tree = etree.HTML(content)
# bus_info = tree.xpath('//div[@class="bus_i_content"]//text()')
# print(bus_info)
# # bus = tree.xpath('//div[@class="bus_line_site "][1]/div/div/a/text()')
# # xia = tree.xpath('//div[@class="bus_line_site "][2]/div/div/a/text()')
# # print(bus)
# # print(xia)
# # 上行总站数
# up_siteTotal = tree.xpath('//div[@class="bus_line_top "][1]/span/text()')[0]
# # 上行站台信息
# up_site_info = tree.xpath('//div[@class="bus_line_site "][1]/div/div/a/text()')
# try :
#     # 下行总站数
#     down_siteTotal = tree.xpath('//div[@class="bus_line_top "][2]/span/text()')
#     # 下行站台信息
#     down_site_info = tree.xpath('//div[@class="bus_line_site "][2]/div/div/a/text()')
# except:
#     down_siteTotal = 0
#     down_site_info = ''
#
# # print(up_siteTotal)
# # print(up_site_info)
# # print(down_siteTotal)
# # print(down_site_info)
# item = []
# items = {
#     '公交线路信息': bus_info,
#     '上行总站数': up_siteTotal,
#     '上行站台信息': up_site_info,
#     '下行总站数': down_siteTotal,
#     '下行站台信息': down_site_info,
# }
# item.append(items)
# for i in items:
#     print(i)


'''
# csv文件读取
csv_file = csv.reader(open('test.csv', 'r'))
# print(csv_file)
for i in csv_file:
    print(i)
'''
# csv文件写入
stu1 = ['公交线路', '运行时间', '票价信息', '公交公司', '最后更新', '上行总站数', '上行站台', '下行总站数', '下行站台']
# stu2 = bus_info + up_siteTotal + up_site_info + down_siteTotal + down_site_info

out = open('test1.csv', 'a+', newline='')
csv_write = csv.writer(out, dialect='excel')
csv_write.writerow(stu1)
# csv_write.writerow(stu2)
# with open('test3.csv', 'a', newline='') as f:
#     csv_write = csv.writer(f, dialect='excel')
#     csv_write.writerow(stu1)
#     csv_write.writerow(stu2)







end = datetime.datetime.now()
print("[ Finished in", (end - start), "]")