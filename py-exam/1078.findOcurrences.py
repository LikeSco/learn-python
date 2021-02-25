#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给出第一个词 first 和第二个词 second，考虑在某些文本 text 中可能以 "first second third" 形式出现的情况，其中 second 紧随 first 出现，third 紧随 second 出现。

对于每种这样的情况，将第三个词 "third" 添加到答案中，并返回答案。
"""


class Solution:
    def findOcurrences(self, text: str, first: str, second: str):
        result = []
        if text.strip() == '':
            return result
        arr = text.split(' ')
        for i in range(len(arr) - 2):
            if arr[i] == first and arr[i + 1] == second:
                result.append(arr[i + 2])
        return result


text = "we will we will rock you"
first = "we"
second = "will"
sol = Solution()
res = sol.findOcurrences(text, first, second)
print(res)
