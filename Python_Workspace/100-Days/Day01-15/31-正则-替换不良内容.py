# -*- coding:utf-8 -*-
# time: 2019/8/12 10:31
# File: 31-正则-替换不良内容.py

import re

def main():
    """
    替换字符串中的不良内容
    :return: 替换后的字符串
    """
    file = "你丫是傻叉吗? 我操你大爷的. Fuck you."
    ret = re.compile(r'傻[叉逼比子狗]|Fuck|shit|[操艹]', re.I) # re.I忽略大小写
    file1 = re.sub(ret, "*", file)
    print(file1)


if __name__ == '__main__':
    main()