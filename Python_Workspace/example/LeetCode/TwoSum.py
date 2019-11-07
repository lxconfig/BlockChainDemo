# -*- coding:utf-8 -*-
# time: 2019/06/25 16:06
# File: TwoSum.py

class Solution:
    def twosum(self, nums, target):
        dict1 = {}
        for i in range(len(nums)):
            j = target- nums[i]
            if j not in dict1:
                dict1[nums[i]] = i
            else:
                return [dict1[nums[i]], i]


s = Solution()
print(s.twosum([2, 5, 5, 11], target=10))
