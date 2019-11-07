# -*- coding:utf-8 -*-
# time:2018/12/03

#string = "FishC"

# it = iter(string)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# it = iter(string)
# while True:
#     try:
#         t = next(it)
#         print(t)
#     except StopIteration:
#         break
# a = 3
# b = 1
# a, b = b, a + b
# print(a, b)

class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a
fibs = Fibs()
for each in fibs:
    if each < 50:
        print(each)