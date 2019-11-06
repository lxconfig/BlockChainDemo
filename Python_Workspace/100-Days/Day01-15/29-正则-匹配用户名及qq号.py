# -*- coding:utf-8 -*-
# time: 2019/8/12 10:02
# File: 29-正则-匹配用户名及qq号.py

import re

def main():
    """
    验证输入用户名和QQ号是否有效并给出对应的提示信息
    要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
    """
    username = str(input("请输入用户名："))
    qq = str(input("请输入QQ号："))
    username_ret = re.compile(r'\w{6,20}') # r'^[0-9a-zA-Z]{6,20}$'
    qq_ret = re.compile(r'[1-9]\d{4,11}')
    u1 = re.match(username_ret, username)
    q1 = re.match(qq_ret, qq)

    if not u1:
        print("请输入正确的用户名")
    if not q1:
        print("请输入正确的QQ号")
    if u1 and q1:
        print("输入正确")


if __name__ == '__main__':
    main()