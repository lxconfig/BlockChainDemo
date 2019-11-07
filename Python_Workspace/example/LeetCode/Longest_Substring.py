# -*- coding:utf-8 -*-
# time: 2019/06/14 13:02
# File: Longest_Substring.py
import pysnooper
class Solution:
    def lengthOfLongestSubstring(self, s: "str") -> "int":
        if len(s):
            result = []
            temp = s[0]
            for i in s[1: ]:
                if i not in temp:
                    temp += i
                elif i == temp[0]:
                    temp = temp[1: ] + i
                elif i == temp[-1]:
                    result.append(temp)
                    temp = i
                else:
                    result.append(temp)
                    temp = temp[temp.find(i) + 1: ] + i
            result.append(temp)
            return len(max(result, key=len))
        return 0



s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))

