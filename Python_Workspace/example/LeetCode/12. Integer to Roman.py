# -*- coding:utf-8 -*-
# time: 2019/07/08 10:13
# File: 12. Integer to Roman.py

class Solution:
    def inttoRoman(self, num):
        Roman = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        Integer = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        result, index = "", len(Integer) - 1
        while num:
            if num - Integer[index] >= 0:
                result += Roman[index]
                num -= Integer[index]
            else:
                index -= 1
        return result


s = Solution()
print(s.inttoRoman(1994))
