# -*- coding:utf-8 -*-
# time: 2019/8/21 9:53
# File: 10-ShellSort.py

class ShellSort:
    """希尔排序"""
    """
    最坏时间复杂度：O(n^2)
    最优时间复杂度：根据步长变化
    稳定性：不稳定
    """
    def __init__(self, item):
        self.__item = item

    def sort(self):
        n = len(self.__item)
        gap = n // 2
        while gap > 0:
            """控制gap变化"""
            for i in range(gap, n):
                """每次从gap,gap+1....开始向前比较"""
                while i > 0:
                    """类似插入排序，比较的间隔变成gap"""
                    if self.__item[i] < self.__item[i-gap]:
                        self.__item[i], self.__item[i-gap] = self.__item[i-gap], self.__item[i]
                        i -= gap
                    else:
                        break
            gap //= 2
        return self.__item


def Shell_Sort(item):
    n = len(item)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            while i > 0:
                if item[i] < item[i-gap]:
                    item[i], item[i-gap] = item[i-gap], item[i]
                    i -= gap
                else:
                    break
        gap //= 2
    return item



if __name__ == '__main__':
    # shell_sort = ShellSort([5, 3, 4, 8, 1, 0, -1, 6, 9, 2, 11])
    # print(shell_sort.sort())
    print(Shell_Sort([5, 3, 4, 8, 1, 0, -1, 6, 9, 2, 11]))