#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。

假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。

注意：每次拼写（指拼写词汇表中的一个单词）时，chars 中的每个字母都只能用一次。

返回词汇表 words 中你掌握的所有单词的 长度之和。
"""


class Solution:
    def countCharacters(self, words, chars: str) -> int:
        length = 0
        for item in words:
            s = list(chars)
            flag = True
            for ch in item:
                if ch in s:
                    s.remove(ch)
                else:
                    flag = False
                    break
            if flag:
                length += len(item)
        return length


words = ["cat", "bt", "hat", "tree"]
chars = "atach"
sol = Solution()
res = sol.countCharacters(words, chars)
print(res)
