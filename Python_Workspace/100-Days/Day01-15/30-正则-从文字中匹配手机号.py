# -*- coding:utf-8 -*-
# time: 2019/8/12 10:14
# File: 30-正则-从文字中匹配手机号.py

import re

def main():
    """
    从这段文字中提取正确的手机号
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765
    :return:
    """
    file = "重要的事情说8130123456789遍，我的手机号是13512346789这个靓号" \
           "不是15600998765，也是110或119，王大锤的手机号才是15600998765"
    ret = re.compile(r'(?<=\D)1[345789]\d{9}')
    number = re.findall(ret, file)
    print(number)


if __name__ == '__main__':
    main()