# -*- coding:utf-8 -*-
# time: 2019/7/31 16:29
# File: 10-寻找2~99之间的素数.py

import time

def prime(num):
    factor = []
    if num == 1:
        return True
    for i in range(1, num+1):
        if num % i == 0:
            factor.append(i)
    if len(factor) == 2:
        print(num, end=" ")



if __name__ == '__main__':
    t1 = time.time()
    for num in range(2, 100):
        prime(num)
    t2 = time.time()
    print(t2 - t1)
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97

# t1 = time.time()
# import math
#
# for num in range(2, 100):
#     is_prime = True
#     for factor in range(2, int(math.sqrt(num)) + 1):
#         if num % factor == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, end=' ')
# t2 = time.time()
# print(t2-t1)