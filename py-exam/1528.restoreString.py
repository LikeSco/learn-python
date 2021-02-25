#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个字符串 s 和一个 长度相同 的整数数组 indices 。

请你重新排列字符串 s ，其中第 i 个字符需要移动到 indices[i] 指示的位置。

返回重新排列后的字符串。
"""


class Solution:
    def restoreString(self, s: str, indices) -> str:
        s1 = list(s)
        for i in range(len(s)):
            s1[indices[i]] = s[i]
        return ''.join(s1)


s = "aiohn"
indices = [3, 1, 4, 2, 0]
sol = Solution()
res = sol.restoreString(s, indices)
print(res)
