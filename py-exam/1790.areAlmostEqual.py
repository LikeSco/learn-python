#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你长度相等的两个字符串 s1 和 s2 。一次 字符串交换 操作的步骤如下：选出某个字符串中的两个下标（不必不同），并交换这两个下标所对应的字符。

如果对 其中一个字符串 执行 最多一次字符串交换 就可以使两个字符串相等，返回 true ；否则，返回 false 。
"""


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        if set(s1) != set(s2):
            return False
        count = 0
        for i in range(len(s1)):
            if count <= 2:
                if s1[i] != s2[i]:
                    count += 1
            else:
                break
        return count == 2


s1 = "bank"
s2 = "kanb"
sol = Solution()
res = sol.areAlmostEqual(s1, s2)
print(res)
