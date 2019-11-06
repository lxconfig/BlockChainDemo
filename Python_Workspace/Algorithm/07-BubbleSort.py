# -*- coding:utf-8 -*-
# time: 2019/8/21 9:08
# File: 07-BubbleSort.py

import time

class BubbleSort:
    """冒泡排序"""
    """
    最坏时间复杂度：O(n^2)
    最优时间复杂度：O(n)
    稳定性：稳定
    """
    def __init__(self, item):
        self.__item = item

    def sort(self):
        n = len(self.__item)
        for j in range(0, n-1):
            """外层循环控制循环比较的次数，每次缩小比较范围"""
            for i in range(0, n-1-j):
                """内层循环控制前后元素比较大小并交换，每次把当前最大的元素沉底"""
                if self.__item[i] > self.__item[i+1]:
                    self.__item[i], self.__item[i+1] = self.__item[i+1], self.__item[i]
        return self.__item

def calc_time(func):
    def wrapper(item):
        t1 = time.time()
        func(item)
        t2 = time.time()
        print(t2-t1)
    return wrapper

# @calc_time
def Bubble_sort(item):
    n = len(item)
    count = 0
    for j in range(0, n-1):
        for i in range(1, n-j):
            if item[i] < item[i-1]:
                item[i], item[i-1] = item[i-1], item[i]
                count += 1
        if count == 0:
            return item
    return item







if __name__ == '__main__':
    # bubble_sort = BubbleSort([10, 5, 3, 4, 8, 1, 0, -1, 2, 6, -3])
    # print(bubble_sort.sort())
    # print(Bubble_sort([10, 5, 3, 4, 8, 1, 0, -3, -1]))
    print(Bubble_sort([0, 1, 3, 4, 5, 8]))