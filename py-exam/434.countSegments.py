#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。

请注意，你可以假定字符串里不包括任何不可打印的字符。
"""


class Solution:
    def countSegments(self, s: str) -> int:
        arr = s.split(' ')
        while '' in arr:
            arr.remove('')
        return len(arr)


s = "Hello, my name is John"
sol = Solution()
res = sol.countSegments(s)
print(res)
