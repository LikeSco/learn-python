#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个二进制字符串 s ，该字符串 不含前导零 。

如果 s 最多包含 一个由连续的 '1' 组成的字段 ，返回 true​​​ 。否则，返回 false 。
"""


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if '01' in s:
            return False
        return True


s = "110110111"
sol = Solution()
res = sol.checkOnesSegment(s)
print(res)
