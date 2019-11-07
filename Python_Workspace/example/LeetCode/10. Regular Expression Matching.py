# -*- coding:utf-8 -*-
# time: 2019/07/01 13:54
# File: 10. Regular Expression Matching.py

class Solution:
    def isMatch(self, s, p):
        if not s and not p: return False
        m = len(s) + 1
        n = len(p) + 1
        dp = [[False] * (m * n)]
        dp[0][0] = True


s = Solution()
print(s.isMatch("a", "."))