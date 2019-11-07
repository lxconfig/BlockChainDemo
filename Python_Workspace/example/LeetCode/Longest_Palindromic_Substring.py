# -*- coding:utf-8 -*-
# time: 2019/06/18 13:44
# File: Longest_Palindromic_Substring.py
import pysnooper


class Solution:
    @pysnooper.snoop(output="log.log", prefix="longestPalindrome")
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            even = self.helper(s, i, i)
            if len(even) > len(res):
                res = even
            odd = self.helper(s, i, i+1)
            if len(odd) > len(res):
                res = odd
        return res

    @pysnooper.snoop(output="log.log", prefix="helper")
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1 : r]

ss = Solution()
print(ss.longestPalindrome("babad"))