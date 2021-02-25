#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。

如果不存在最后一个单词，请返回 0。
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s.replace(" ", "")) == 0:
            return 0
        arr = s.split(' ')
        dict_word = []
        for item in arr:
            if len(item) > 0:
                dict_word.append(item)
        lastWord = dict_word.pop()
        return len(lastWord)


s = 'Hello World    '
sol = Solution()
res = sol.lengthOfLastWord(s)
print(res)
