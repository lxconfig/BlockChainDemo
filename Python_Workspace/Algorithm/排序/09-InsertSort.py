# -*- coding:utf-8 -*-
# time: 2019/8/21 9:41
# File: 09-InsertSort.py

class InsertSort:
    """插入排序"""
    """
    最坏时间复杂度：O(n^2)
    最优时间复杂度：O(n)
    稳定性：稳定
    """
    def __init__(self, item):
        self.__item = item

    def sort(self):
        n = len(self.__item)
        for i in range(1, n):
            """外层循环控制比较开始的位置"""
            index = i
            while index > 0:
                """内层循环元素进行比较交换"""
                if self.__item[index] < self.__item[index-1]:
                    self.__item[index], self.__item[index-1] = self.__item[index-1], self.__item[index]
                    index -= 1
                else:
                    break
        return self.__item

def Insert_Sort(item):
    n = len(item)
    for j in range(1, n-1):
        index = j
        while index > 0:
            if item[index] < item[index-1]:
                item[index], item[index-1] = item[index-1], item[index]
                index -= 1
            else:
                break
    return item


if __name__ == '__main__':
    # insert_sort = InsertSort([5, 3, 4, 8, 1, 0, 10, 6, 7, -1])
    # print(insert_sort.sort())

    print(Insert_Sort([5, 3, 4, 8, 1, 0, 10, 6, 7, -1]))