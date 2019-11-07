# -*- coding:utf-8 -*-
# time: 2019/06/25 20:19
# File: 装饰器.py
# class A():
#     bar = 1
#     def foo(self):
#         print("foo")
#
#     @staticmethod
#     def static_foo():
#         print("static_foo")
#         print(A.bar)
#
#     @classmethod
#     def class_foo(cls):
#         print("class_foo")
#         print(cls.bar)
#         print(cls().foo())
#
# A().foo()
# A.static_foo()
# A.class_foo()

# import time
#
# def display(func):
#     def calc_time(*args):
#         t1 = time.time()
#         func(*args)
#         t2 = time.time()
#         print(t2 - t1)
#     return calc_time
#
#
# @display
# def show(num):
#     for i in range(num):
#         print(i**i)
#
# # print(show(1000))
# show(299)

def func1():
    print("------func1-----")

def outer(func):
    def inner():
        print("------inter------")
        func()
    return inner

f = outer(func1)
print(type(f))
f()