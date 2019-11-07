# -*- coding:utf-8 -*-
# time:2019/02/26 19:28

import jsonpath
import json

# 将json格式字符串转化为python对象
obj = json.load(open("book.json", 'r', encoding="utf8"))
print(obj)

# 书店所有的作者
# 根元素下一级的store节点，store节点下一级的book节点，book节点中的所有节点中的author节点
ret_1 = jsonpath.jsonpath(obj, '$.store.book[*].author')
print(ret_1)

# 所有的作者
# 根元素下任意位置的author节点
ret_2 = jsonpath.jsonpath(obj, '$..author')
print(ret_2)

# store的所有元素，所有book和bicycle
# 也可写成'$.store.*'
ret_3 = jsonpath.jsonpath(obj, '$.store[*]')
print(ret_3)

# store里面所有东西的price
ret_4 = jsonpath.jsonpath(obj, '$.store..price')
print(ret_4)

# 第三本书
# 也可写成'$..book[2]'
ret_5 = jsonpath.jsonpath(obj, '$.store.book[2]')
print(ret_5)

# 最后一本书
ret_6 = jsonpath.jsonpath(obj, '$..book[(@.length - 1)]')
print(ret_6)

# 前两本书
# 也可写成'$..book[0,1]' , '$..book[:2]'
ret_7 = jsonpath.jsonpath(obj, '$.store.book[0,1]')
print(ret_7)

# 过滤出所有包含isbn的书
ret_8 = jsonpath.jsonpath(obj, '$..book[?(@.isbn)]')
print(ret_8)

# 过滤出所有价格低于10的书
# 也可写成'$..book[?(@.price < 10)]'
ret_9 = jsonpath.jsonpath(obj, '$.store.book[?(@.price < 10)]')
print(ret_9)

# 所有元素
ret_10 = jsonpath.jsonpath(obj, '$.*')
print(ret_10)