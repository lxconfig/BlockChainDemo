# -*- coding:utf-8 -*-
# time: 2019/7/31 14:40
# File: 03-判断是否是闰年.py

def is_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_leap(2020))