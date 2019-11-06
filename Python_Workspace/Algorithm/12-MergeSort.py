# -*- coding:utf-8 -*-
# time: 2019/8/21 14:49
# File: 12-MergeSort.py


def MergeSort(item):
    """归并排序"""
    """
    空间复杂度：O(n)
    最坏时间复杂度：O(nlogn)
    最优时间复杂度：O(nlogn)
    稳定性：稳定
    """
    n = len(item)
    mid = n // 2
    if n <= 1:
        return item
    # 将列表划分为子序列，直到子序列中只有一个元素为止
    left = MergeSort(item[:mid])
    right = MergeSort(item[mid:])
    left_pointer, right_pointer = 0, 0
    result = []
    while left_pointer < len(left) and right_pointer < len(right):
        """对子序列中的元素进行比较，合并"""
        if left[left_pointer] <= right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1
    # 将剩余元素添加到结果中
    result += left[left_pointer:]
    result += right[right_pointer:]
    return result

if __name__ == '__main__':
    li = [5, 3, 4, 8, 1, 0, 2, -1, -2]
    merge_sort = MergeSort(li)
    print(merge_sort)