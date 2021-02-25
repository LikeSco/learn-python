#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        for ch in s:
            if s.count(ch) == 1:
                return s.index(ch)
        return -1


s = "a good day"
sol = Solution()
res = sol.firstUniqChar(s)
print(res)
