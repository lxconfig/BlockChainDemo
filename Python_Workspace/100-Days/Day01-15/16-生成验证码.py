# -*- coding:utf-8 -*-
# time: 2019/8/6 14:08
# File: 16-生成验证码.py

import random

def main(length):
    """
    生成指定长度的验证码
    :param length: 验证码长度
    :return: 验证码（可能包含大小写字母和数字）
    """
    all_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    code = ""
    for i in range(0, length):
        index = random.randint(0, len(all_chars)-1)
        code += all_chars[index]
    return code



if __name__ == '__main__':
    length = int(input("请输入验证码长度："))
    print(main(length))