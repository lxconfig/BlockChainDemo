# -*- coding:utf-8 -*-
# time: 2019/07/08 9:54
# File: 11.Container With Most Water.py
import pysnooper
class Solution:
    @pysnooper.snoop(output="contaniner.log")
    def maxArea(self, height):
        L, R, width, result = 0, len(height)-1, len(height)-1, 0
        for w in range(width, 0, -1):
            if height[L] < height[R]:
                result, L = max(result, height[L] * w), L+1
            else:
                result, R = max(result, height[R] * w), R-1
        return result

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))