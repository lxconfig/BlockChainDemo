# -*- coding:utf-8 -*-
# time: 2019/7/31 14:37
# File: 02-计算圆的周长和面积.py

def calc(r):
    perimeter = 2 * 3.14 * r
    area = 3.14 * r ** 2
    print("周长为：%1.f, 面积为：%1.f" % (perimeter, area))


if __name__ == '__main__':
    calc(3)