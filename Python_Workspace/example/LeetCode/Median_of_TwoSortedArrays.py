# -*- coding:utf-8 -*-
# time: 2019/06/17 19:13
# File: Median_of_TwoSortedArrays.py

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if not nums1:
            n = len(nums2)
            if n % 2 == 0:  # nums2为偶数个元素
                median = (float(nums2[n//2]) + float(nums2[n//2 - 1])) / 2
                return median
            else:  # nums2为奇数个元素
                median = float(nums2[n // 2])
                print(type(median))
                return median

        if not nums2:
            m = len(nums1)
            if m % 2 == 0:  # nums1为偶数个元素
                median = (float(nums1[m//2]) + float(nums1[m//2 - 1])) / 2
                return median
            else:  # nums1为奇数个元素
                median = float(nums1[m // 2])
                return median


        if nums1 and nums2:
            m, n = len(nums1), len(nums2)
            lens = m + n
            if n < m:
                for i in nums2:
                    nums1.append(i)
                nums1.sort()
                if lens % 2 == 0:
                    median = (float(nums1[lens//2]) + float(nums1[lens//2 - 1])) / 2
                    return median
                else:
                    median = float(nums1[lens // 2])
                    return median
            else:
                for i in nums1:
                    nums2.append(i)
                nums2.sort()
                if lens % 2 == 0:
                    median = (float(nums2[lens//2]) + float(nums2[lens//2 - 1])) / 2
                    return median
                else:
                    median = float(nums2[lens // 2])
                    return median


class Solutions:
    def Median(self, nums1, nums2):
        if nums1 and nums2:
            nums1 = nums1 + nums2
            nums1.sort()
            length = len(nums1)
            if length % 2 == 0:
                temp = length // 2
                median = (float(nums1[temp - 1]) + float(nums1[temp])) / 2
                return median
            else:
                temp = length // 2
                median = float(nums1[temp])
                return median
        elif nums1:
            length = len(nums1)
            if length % 2 == 0:
                temp = length // 2
                median = (float(nums1[temp - 1]) + float(nums1[temp])) / 2
                return median
            else:
                temp = length // 2
                median = float(nums1[temp])
                return median
        elif nums2:
            length = len(nums2)
            if length % 2 == 0:
                temp = length // 2
                median = (float(nums2[temp - 1]) + float(nums2[temp])) / 2
                return median
            else:
                temp = length // 2
                median = float(nums2[temp])
                return median
        else:
            return 0.0

s = Solutions()
nums11 = [1, 2]
nums22 = [3, 4]
print(s.Median(nums11, nums22))


