# -*- coding:utf-8 -*-
# time: 2019/06/26 18:45
# File: 判断回文字符串.py

def huiwen(s):
    res = s[::-1]
    if res == s:
        return "是"
    return "不是"

if __name__ == '__main__':
    print(huiwen("bba"))