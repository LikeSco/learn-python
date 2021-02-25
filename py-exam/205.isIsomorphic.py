#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_ch = {}
        t1 = ''
        for i in range(len(s)):
            if s[i] in dict_ch.keys():
                t1 += dict_ch[s[i]]
            elif t[i] in dict_ch.values():
                return False
            else:
                dict_ch[s[i]] = t[i]
                t1 += t[i]

        if t1 == t:
            return True
        else:
            return False


s = "paper"
t = "title"
sol = Solution()
res = sol.isIsomorphic(s, t)
print(res)
