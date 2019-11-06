# coding:utf-8
# time: 2019/8/23 10:51
# File: 13-BinarySearch.py

def BinarySearch(item, value):
    """二分查找(递归形式)"""
    n = len(item)
    mid = n // 2
    if n > 0:
        if item[mid] == value:
            return True
        elif item[mid] > value:
            return BinarySearch(item[:mid], value)
        else:
            return BinarySearch(item[mid+1:], value)
    return False

def BinarySearch2(item, value):
    """二分查找(非递归形式)"""
    n = len(item)
    first, last = 0, n-1
    while first <= last:
        mid = (first + last) // 2
        if item[mid] == value:
            return True
        elif item[mid] > value:
            last = mid - 1
        else:
            first = mid + 1
    return False

if __name__ == '__main__':
    li = [1, 3, 4, 5, 6, 8]
    # print(BinarySearch(li, 8))
    # print(BinarySearch(li, 3))
    print(BinarySearch2(li, 3))
    print(BinarySearch2(li, 7))