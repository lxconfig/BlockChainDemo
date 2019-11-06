# -*- coding:utf-8 -*-
# time: 2019/7/31 15:39
# File: 07-生成斐波那契数列.py

def fib(n):
    a, b = 1, 0
    for _ in range(1, n):
        a, b = b, a+b
        print(b)


if __name__ == '__main__':
    fib(10)