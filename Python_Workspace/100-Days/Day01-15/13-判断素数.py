# -*- coding:utf-8 -*-
# time: 2019/8/6 13:46
# File: 13-判断素数.py

def is_prime(num):
    if num == 1:
        return True
    factor = []
    for i in range(1, num + 1):
        if num % i == 0:
            factor.append(i)
    if len(factor) == 2:
        return True
    else:
        return False



if __name__ == '__main__':
    num = int(input("请输入数字："))
    print(is_prime(num))