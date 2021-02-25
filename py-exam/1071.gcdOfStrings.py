#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
对于字符串 S 和 T，只有在 S = T + ... + T（T 自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。

返回最长字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。
"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str1 in str2) or (str2 in str1):
            s1 = str1 + str2 + str2
            if (str1 in s1[1:-1]) and (str2 in s1[1:-1]):
                while 1:
                    if len(str1) == len(str2):
                        return str1
                    if len(str1) > len(str2):
                        str1 = str1[len(str2):]
                    else:
                        str2 = str2[len(str1):]

        return ''


str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
sol = Solution()
res = sol.gcdOfStrings(str1, str2)
print(res)
