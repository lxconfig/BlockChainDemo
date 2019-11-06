# -*- coding:utf-8 -*-
# time: 2019/8/21 10:10
# File: 11-QuickSort.py

class QuickSort:
    """快速排序"""
    """
    最坏时间复杂度：O(n^2)
    最优时间复杂度：O(nlogn)
    稳定性：不稳定
    """
    def __init__(self, item):
        self.__item = item

    def sort(self, first, last):
        if first >= last:
            return self.__item
        low, high = first, last
        mid = self.__item[first]
        while low < high:
            while low < high and self.__item[high] <= mid:
                high -= 1
            self.__item[low] = self.__item[high]

            while low < high and self.__item[low] > mid:
                low += 1
            self.__item[high] = self.__item[low]
        self.__item[low] = mid

        # 递归
        self.sort(first, low-1)
        self.sort(low+1, last)
        return self.__item





if __name__ == '__main__':
    li = [5, 3, 4, 8, 1, 0, 2, -1, -2]
    quick_sort = QuickSort(li)
    print(quick_sort.sort(0, len(li)-1))