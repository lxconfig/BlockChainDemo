# -*- coding:utf-8 -*-
# time:2018/12/28 14:57
from bs4 import BeautifulSoup

# 生成对象
soup = BeautifulSoup(open("soup-text.html", encoding="utf-8"), 'lxml')
# print(type(soup))
# print(soup)

# 通过标签名查找,只能找到第一个
# print(soup.div)

# 获取标签属性值
# print(soup.a['href'])
# print(soup.a['title'])
# print(soup.a.attrs)
# print(soup.a.attrs['href'])

# 获取内容
# print(soup.a.text)
# print(soup.a.string)
# print(soup.a.get_text())
# print(soup.div.text)
# print(soup.div.string)
# print(soup.div.get_text())

# find方法
print(soup.find('a', class_='du'))

# find_all方法
# print(soup.find_all('a'))

# select方法
# print(soup.select('.tang > ul > li > a'))
# print(soup.select('.tang > ul > li > a')[2])
# div = soup.select('.tang > ul > li > a')[2]
# print(div['href'])
# print(soup.select('.du')[0]['href'])