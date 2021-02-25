#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。
"""


class Solution:
    def toLowerCase(self, str: str) -> str:
        ascii_lower = 'abcdefghijklmnopqrstuvwxyz'
        ascii_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        dict_ascii = {}
        for i in range(len(ascii_lower)):
            dict_ascii[ascii_upper[i]] = ascii_lower[i]

        for ch in str:
            if ch in dict_ascii.keys():
                str = str.replace(ch, dict_ascii[ch])
        return str


s = "LoVELY"
sol = Solution()
res = sol.toLowerCase(s)
print(res)
