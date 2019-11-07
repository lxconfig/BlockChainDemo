# -*- coding:utf-8 -*-
# time: 2019/06/05 14:27
# File: demo.py
count_string = "ab2b3n5n2n67mm4n2"
# i = 0
# for string in count_string:
#     if string == "n":
#         i += 1
#
# print(i)

# print(len(count_string.split("n")) - 1)

import random

# list1 = [x for x in (random.randint(1, 50) for i in range(50)) if x % 2 ==0]
# print(len(list1))
# print(list1)
list1 = list()
for i in range(50):
    num = random.randint(1, 50)
    if num % 2 ==0:
        list1.append(num)
print(list1)



a = 10
while a:
    if a % 10 == 0:
        print("---if")
        a += 1
    elif a % 10 == 1:
        print("---elif")
        a += 1

    else:
        print("---else")
        break