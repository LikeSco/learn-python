#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个字符串，逐个翻转字符串中的每个单词。
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        # if len(s.strip()) == 0:
        #     return ''
        arr = s.split(' ')
        word_list = []
        for item in arr:
            if len(item) > 0:
                word_list.append(item)
        word_list.reverse()
        return ' '.join(word_list)


s = " Alice does not even like bob "
sol = Solution()
res = sol.reverseWords(s)
print(res)
