# -*- coding:utf-8 -*-
# time: 2019/8/4 9:53
# File: 11-最大公约数和最小公倍数.py

def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    return x * y // gcd(x, y)



if __name__ == '__main__':
    print(gcd(21, 28))
    print(lcm(21, 28))