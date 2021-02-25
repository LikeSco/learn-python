#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定两个句子 A 和 B 。 （句子是一串由空格分隔的单词。每个单词仅由小写字母组成。）

如果一个单词在其中一个句子中只出现一次，在另一个句子中却没有出现，那么这个单词就是不常见的。

返回所有不常用单词的列表。

您可以按任何顺序返回列表。
"""


class Solution:
    def uncommonFromSentences(self, A: str, B: str):
        arrA = A.split(' ')
        arrB = B.split(' ')
        arr = arrA + arrB
        result = []
        for word in arr:
            if arr.count(word) == 1:
                result.append(word)
        return result


A = "this apple is sweet"
B = "this apple is sour"
sol = Solution()
res = sol.uncommonFromSentences(A, B)
print(res)
