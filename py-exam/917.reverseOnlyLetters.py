#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。
"""
import re


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        ascii_ch = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        dict_S = {}
        for i, ch in enumerate(S):
            dict_S[i] = ch
        S1 = re.sub('[^' + ascii_ch + ']', '', S)
        list_S = list(S1)
        S2 = ''
        for i in dict_S:
            if dict_S[i] in ascii_ch:
                val = list_S.pop()
                S2 += val
            else:
                S2 += dict_S[i]
        return S2


S = "Test1ng-Leet=code-Q!"
sol = Solution()
res = sol.reverseOnlyLetters(S)
print(res)
