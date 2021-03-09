#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。

美式键盘 中：

第一行由字符 "qwertyuiop" 组成。
第二行由字符 "asdfghjkl" 组成。
第三行由字符 "zxcvbnm" 组成。
"""


class Solution:
    def findWords(self, words):
        keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        result = []
        for word in words:
            word1 = word.lower()
            for key in keyboard:
                flag = True
                for s in word1:
                    if s not in key:
                        flag = False
                        break
                if flag:
                    result.append(word)
                    break
        return result


words = ["Hello", "Alaska", "Dad", "Peace"]
sol = Solution()
res = sol.findWords(words)
print(res)
