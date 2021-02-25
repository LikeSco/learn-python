#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
在一个「平衡字符串」中，'L' 和 'R' 字符的数量是相同的。

给出一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。

返回可以通过分割得到的平衡字符串的最大数量。
"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:

        list_s = []
        while len(s) > 0:
            i = 0
            for i in range(i, len(s)):
                s1 = s[0:i + 2]
                if s1.count('R') == s1.count('L'):
                    list_s.append(s1)
                    if len(s1) == len(s):
                        s = ''
                    else:
                        s = s[i + 2:]
                    break

        return len(list_s)


s = "RLRRLLRLRL"
sol = Solution()
res = sol.balancedStringSplit(s)
print(res)
