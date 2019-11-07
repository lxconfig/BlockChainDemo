# -*- coding:utf-8 -*-
# time: 2019/06/19 20:39
# File: ZigZag_Conversion.py
import pysnooper
class Solution:
    @ pysnooper.snoop(output="log.log")
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        l = [""] * numRows
        index, step = 0, 1
        for i in s:
            l[index] += i
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return "".join(l)  # 用""字符将原来的字符（每个元素）拼接起来形成新的字符串
s = Solution()
print(s.convert("PAYPALISHIRING", 4))
