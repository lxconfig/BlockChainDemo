# -*- coding:utf-8 -*-
# time: 2019/03/18 14:44
# File: 12-queue.py
import datetime
from queue import Queue

start = datetime.datetime.now()

# 创建队列
q = Queue(5)
# 判空
# print(q.empty())
# 判满
# print(q.full())
# 获取队列长度
# print(q.qsize())

# 存数据
q.put('kobe')
q.put('qwe')
q.put('123')
q.put("zxc")
q.put("asd")
# print(q.empty())
# print(q.full())
# print(q.qsize())

# 取数据
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
end = datetime.datetime.now()
print("[ Finished in", (end - start), "]")