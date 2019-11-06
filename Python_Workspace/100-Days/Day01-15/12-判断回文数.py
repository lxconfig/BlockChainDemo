# -*- coding:utf-8 -*-
# time: 2019/8/6 13:38
# File: 12-判断回文数.py
# import pysnooper


# @pysnooper.snoop(output="log.log")
def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num




if __name__ == '__main__':
    num = int(input("请输入数字："))
    print(is_palindrome(num))