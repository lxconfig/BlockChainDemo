# -*- coding:utf-8 -*-
# time: 2019/7/12 15:44
# File: 14. Longest Common Prefix.py

class Solution:
    def longestCommonPrefix(self, strs):
        # zip(*strs)表示按strs中最短的元素计算，解压为[(),()...()]的形式
        # zip(strs)表示将strs中的元素转换为一个个的元组[(,),(,)...(,)]，如果是多个参数，则取短的个数
        temp = zip(*strs)
        result = ""
        for i in temp:
            if len(set(i)) > 1: break   # set(i)创建一个不重复元素的集合，全是相同元素len(set(i))=1
            result += i[0]
        # return set(temp)
        return result


s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))