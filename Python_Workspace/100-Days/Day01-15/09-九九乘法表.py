# -*- coding:utf-8 -*-
# time: 2019/7/31 16:24
# File: 09-九九乘法表.py


def table():
    for i in range(1, 10):
        for j in range(1, i + 1):
            x = i * j
            print("%dx%d=%d" % (i, j, x), end='\t')
        print()


if __name__ == '__main__':
    table()