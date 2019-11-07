# -*- coding:utf-8 -*-
# time:2019/01/29 18:38

from lxml import etree

# 生成对象
tree = etree.parse('xpath.html')
# print(tree)

# 取文本
ret = tree.xpath('//div[@class="tang"]/ul/li[1]') # 返回一个列表
print(ret[0].text)

ger = tree.xpath('//div[@class="song"]/text()')
print(ger)

het = tree.xpath('//div[@class="song"]')
string = het[0].xpath('string(.)')  # 当成字符串
print(string)
print(string.replace('\n', '').replace('\t', ''))

# //text()输出div中所有内容，即使内容被标签括起
ge = tree.xpath('//div[@class="song"]//text()')
print(ge)

# 取属性
re = tree.xpath('//div[@class="tang"]/ul/li[last()]/a/@href')
print(re[0])

# 逻辑运算
r = tree.xpath('//div[@class="tang"]/ul/li[@name="shang" and @id="ihua"]')
print(r[0].text)

# contains()
e = tree.xpath('//div[@class="tang"]/ul/li[contains(@name, "s")]/text()')

# 也可匹配包含特定内容的标签
h = tree.xpath('//li[contains(text(), "爱")]/text()')
print(e)
print(h)

# starts-with()
rets = tree.xpath('//div[@class="tang"]/ul/li[starts-with(@id, "i")]/text()')

# 也可匹配以特定内容开头的标签
hrets = tree.xpath('//li[starts-with(text(), "爱")]/text()')
print(rets)
print(hrets)