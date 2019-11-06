# -*- coding:utf-8 -*-
# time: 2019/7/31 14:34
# File: 01-华氏度转摄氏度.py


def FtoC(f):
    c = (f - 32) / 1.8
    print("%.1f" %c)


if __name__ == '__main__':
    FtoC(90)