# -*- coding:utf-8 -*-
# time: 2019/7/31 15:09
# File: 05-寻找完全数.py

# 完全数：一个数的所有因子之和（不包括这个数本身）等于这个数

def find_perfect_number(num):
    factor = []
    for i in range(1, num + 1):
        """寻找每个数的因子"""
        if num % i == 0:
            factor.append(i)

    sum = 0
    for i in factor[0: -1]:
        """因子（除num本身）求和"""
        sum += i

    if sum == num:
        print(num)



if __name__ == '__main__':
    for num in range(1, 10000):
        """寻找三位数中的完全数"""
        find_perfect_number(num)