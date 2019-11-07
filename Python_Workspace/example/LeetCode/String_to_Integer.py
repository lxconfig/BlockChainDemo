# -*- coding:utf-8 -*-
# time: 2019/06/30 13:19
# File: String_to_Integer.py
import re
class Solution:
    def myAtoi(self, str):
        str = str.strip()
        str = re.findall('(^[\+\-0]*\d+)\D*', str)
        print(str)
        try:
            result = int(''.join(str))
            return max(-2 ** 31, min(result, 2 ** 31 - 1))
        except:
            return 0


s = Solution()
print(s.myAtoi("words and 987"))