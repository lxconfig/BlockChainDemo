# -*- coding:utf-8 -*-
# time: 2019/7/12 14:44
# File: 13. Roman to Integer.py
import pysnooper

class Solution:
    @pysnooper.snoop(output="log.log")
    def romanToInt(self, s):
        Roman = {
             "I": 1,
             "IV": 4,
             "V": 5,
             "IX": 9,
             "X": 10,
             "XL": 40,
             "L": 50,
             "XC": 90,
             "C": 100,
             "CD": 400,
             "D": 500,
             "CM": 900,
             "M": 1000
        }
        result, temp = 0, 0

        for i in range(len(s)):
            if temp >= len(s):
                break
            if s[temp: temp+2] in Roman:
                result += Roman[s[temp: temp+2]]
                temp += 2
            elif s[temp] in Roman:
                result += Roman[s[temp]]
                temp += 1
        return result



s = Solution()
print(s.romanToInt("LVIII"))