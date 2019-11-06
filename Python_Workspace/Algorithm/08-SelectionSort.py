# -*- coding:utf-8 -*-
# time: 2019/8/21 9:17
# File: 08-SelectionSort.py

class SelectionSort:
    """选择排序：每次从列表中找到当前最小的值，置于列表前端"""
    """
    最坏时间复杂度：O(n^2)
    最优时间复杂度：O(n^2)
    稳定性：不稳定(升序每次把最大的放到末尾[26, 11, 13, 16, 26, 10, 9])
    """
    def __init__(self, item):
        self.__item = item

    def sort(self):
        n = len(self.__item)
        for j in range(0, n-1):
            """外层循环控制循环比较开始的元素"""
            min = j
            for i in range(j+1, n):
                """内层循环控制元素比较，找到当前最小的元素并交换位置"""
                if self.__item[min] > self.__item[i]:
                    min = i
            self.__item[min], self.__item[j] = self.__item[j], self.__item[min]

        return self.__item

def Selection_Sort(item):
    n = len(item)
    for j in range(0, n-1):
        min_index = j
        for i in range(j+1, n):
            if item[i] < item[min_index]:
                min_index = i
        item[min_index], item[j] = item[j], item[min_index]

    return item


if __name__ == '__main__':
    # selection_sort = SelectionSort([5, 3, 4, 8, 1, 0])
    # print(selection_sort.sort())
    print(Selection_Sort([5, 3, 4, 8, 1, 0]))

