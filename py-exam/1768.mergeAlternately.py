#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你两个字符串 word1 和 word2 。请你从 word1 开始，通过交替添加字母来合并字符串。如果一个字符串比另一个字符串长，就将多出来的字母追加到合并后字符串的末尾。

返回 合并后的字符串 。
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        list_word1 = list(word1)
        list_word2 = list(word2)
        list_word1.reverse()
        list_word2.reverse()
        results = []
        while len(list_word1) + len(list_word2) != 0:
            if len(list_word1) != 0:
                results.append(list_word1.pop())
            if len(list_word2) != 0:
                results.append(list_word2.pop())
        return ''.join(results)


word1 = "ab"
word2 = "pqrs"
sol = Solution()
res = sol.mergeAlternately(word1, word2)
print(res)
