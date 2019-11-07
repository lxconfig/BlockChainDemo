# -*- coding:utf-8 -*-
# time:2018/12/09
def myGen():
    print("生成器执行！")
    yield 1
    yield 2

m = myGen()
for i in m:
    print(i)