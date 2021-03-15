#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给出一个字符串数组words组成的一本英语词典。从中找出最长的一个单词，该单词是由words词典中其他单词逐步添加一个字母组成。若其中有多个可行的答案，则返回答案中字典序最小的单词。

若无答案，则返回空字符串。
"""


class Solution:
    def longestWord(self, words) -> str:
        result = ''
        words.sort()
        words.sort(key=lambda x: len(x))
        words.reverse()
        for word in words:
            s = ''
            if len(word) >= len(result):
                flag = True
                for ch in word:
                    s += ch
                    if s not in words:
                        flag = False
                        break
                if flag:
                    result = word
            else:
                break

        return result


words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
sol = Solution()
res = sol.longestWord(words)
print(res)
