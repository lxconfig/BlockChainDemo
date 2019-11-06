# -*- coding:utf-8 -*-
# time: 2019/8/6 13:51
# File: 14-判断回文素数.py

def is_prime(num):
    factor = []
    if num == 1:
        return True
    for i in range(1, num + 1):
        if num % i == 0:
            factor.append(i)
    if len(factor) == 2:
        return True
    else:
        return False


def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num

def is_palindrome_prime(num):
    if is_prime(num) and is_palindrome(num):
        return True
    else:
        return False


if __name__ == '__main__':
    num = int(input("请输入数字："))
    print(is_palindrome_prime(num))