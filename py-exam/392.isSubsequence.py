#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
"""
import re


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s in t:
            return True
        t1 = re.sub('[^' + s + ']', '', t)

        if s in t1:
            return True

        t2 = ''
        for ch in t1:
            if ch not in t2:
                t2 += ch

        s1 = ''
        for ch1 in s:
            if ch1 not in s1:
                s1 += ch1

        if t2 == s1 and len(s) <= len(t1):
            return True

        return False


s = "abc"
t = "ahbgdc"
sol = Solution()
res = sol.isSubsequence(s, t)
print(res)
