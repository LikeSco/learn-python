#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个字符串 s ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。

请你返回字符串的能量。
"""


class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 1:
            return 1
        list_s = []
        list_count = []
        i = 0
        while i < len(s) - 1:
            while s[i] == s[i + 1]:
                list_s.append(s[i])
                i += 1
                if i >= len(s) - 1:
                    break
            list_count.append(len(list_s) + 1)
            list_s = []
            i += 1
        return max(list_count)


s = "abbcccddddeeeeedcba"
sol = Solution()
res = sol.maxPower(s)
print(res)
