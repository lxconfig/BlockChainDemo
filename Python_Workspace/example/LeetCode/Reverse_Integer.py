# -*- coding:utf-8 -*-
# time: 2019/06/20 13:58
# File: Reverse_Integer.py


class Solution:
    def reverses(self, x):
        if str(x)[0] == "-":
            res = int("-{}".format(str(x)[1: ][::-1]))
        else:
            res = int(str(x)[::-1])
        if res <= -2**31 or res >= 2**31-1:
            return 0
        return res


s = Solution()
print(s.reverses(901000))
# s.reverses(123)