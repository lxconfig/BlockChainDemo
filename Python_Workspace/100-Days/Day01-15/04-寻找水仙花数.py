# -*- coding:utf-8 -*-
# time: 2019/7/31 14:47
# File: 04-寻找水仙花数.py

# 水仙花数：各位上的数字的三次方之和等于原数字

import time
#
# def display_time(func):
#     def wrapper(*args):
#         t1 = time.time()
#         func(*args)
#         t2 = time.time()
#         print(t2 - t1)
#     return wrapper

# @display_time
def find_Narcissistic(num):
    c = num % 10 # 个位
    b = num % 100 // 10 # 十位
    a = num // 100 # 百位
    if a ** 3 + b ** 3 + c ** 3 == num:
        print(num)



if __name__ == '__main__':
    t1 = time.time()
    for num in range(100, 1000):
        """寻找三位数中的水仙花数"""
        find_Narcissistic(num)
    t2 = time.time()
    print(t2 - t1)