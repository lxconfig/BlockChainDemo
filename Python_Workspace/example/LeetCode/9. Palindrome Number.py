# -*- coding:utf-8 -*-
# time: 2019/07/01 13:24
# File: 9. Palindrome Number.py
import pysnooper

class Solution:
    @pysnooper.snoop(output="Palindrome Number.log")
    def isPalindrome(self, x):
        # if str(x) == str(x)[::-1]:
        #     return True
        # else:
        #     return False
        if x < 0:
            return False

        ranger = 1
        while x / ranger >= 10:
            ranger *= 10

        while x:
            left = x / ranger
            right = x % 10
            if left != right:
                return False

            x = (x % ranger) / 10
            ranger /= 100

        return True


s = Solution()
print(s.isPalindrome(+12))

