#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个仅由字符 '0' 和 '1' 组成的字符串 s 。一步操作中，你可以将任一 '0' 变成 '1' ，或者将 '1' 变成 '0' 。

交替字符串 定义为：如果字符串中不存在相邻两个字符相等的情况，那么该字符串就是交替字符串。例如，字符串 "010" 是交替字符串，而字符串 "0100" 不是。

返回使 s 变成 交替字符串 所需的 最少 操作数。
"""


class Solution:
    def minOperations(self, s: str) -> int:
        diff1 = diff2 = 0
        for i, a in enumerate(s):
            if a == "1":
                diff1 += i % 2 == 0
                diff2 += i % 2 == 1
            else:
                diff1 += i % 2 == 1
                diff2 += i % 2 == 0
        return min(diff1, diff2)


s = "0010010"
sol = Solution()
res = sol.minOperations(s)
print(res)
