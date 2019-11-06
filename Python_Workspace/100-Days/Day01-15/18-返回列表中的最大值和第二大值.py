# -*- coding:utf-8 -*-
# time: 2019/8/6 14:39
# File: 18-返回列表中的最大值和第二大值.py

import random

def main(list1):
    """
    返回列表最大值和第二大值
    :param list1: 随机生成的列表
    :return: 最大值和第二大值
    """
    x, y = (list1[0], list1[1]) if list1[0] > list1[1] else (list1[1], list1[0])  # x=11 y=4
    for i in list1[2:]:
        if i > x:
            y = x
            x = i
        elif i > y:
            y = i
    return x,y



if __name__ == '__main__':
    list1 = [random.randint(1, x+10) for x in range(1, 10)]
    print(list1)
    print(main(list1))