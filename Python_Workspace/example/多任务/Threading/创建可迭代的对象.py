# -*- coding:utf-8 -*-
# time: 2019/05/14 20:40
# File: 创建可迭代的对象.py
import collections

class Classmate():
    def __init__(self):
        self.names = list()
        self.current_num = 0
    def add(self, name):
        self.names.append(name)
    def __iter__(self):
        return self
    def __next__(self):
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration

classmate = Classmate()
classmate.add("tewt")
classmate.add("ateerue")
classmate.add("uieotj")
for i in classmate:
    print(i)