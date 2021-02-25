#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）。

字符串 text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "balloon"。
"""


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = 0
        word = 'balloon'
        list_word = list(word)
        list_text = list(text)
        while ('b' in list_text) and ('a' in list_text) and ('l' in list_text) and ('o' in list_text) and ('n' in list_text):
            for item in list_text[:]:
                if item in list_word:
                    list_word.remove(item)
                    list_text.remove(item)
                if len(list_word) == 0:
                    count += 1
                    list_word = list(word)
                    break
        return count


text = "loonbalxballpoon"
sol = Solution()
res = sol.maxNumberOfBalloons(text)
print(res)
