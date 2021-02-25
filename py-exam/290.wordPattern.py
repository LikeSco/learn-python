#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split(' ')
        if len(pattern) != len(arr):
            return False
        dict_ch = {}
        t = ''
        for i in range(len(pattern)):
            if arr[i] in dict_ch.keys():
                t += dict_ch[arr[i]]
            elif pattern[i] in dict_ch.values():
                return False
            else:
                dict_ch[arr[i]] = pattern[i]
                t += pattern[i]

        if t == pattern:
            return True
        else:
            return False


pattern = "abba"
s = "dog cat cat dog"
sol = Solution()
res = sol.wordPattern(pattern, s)
print(res)
