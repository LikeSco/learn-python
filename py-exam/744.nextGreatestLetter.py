#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。另给出一个目标字母 target，请你寻找在这一有序列表里比目标字母大的最小字母。

在比较时，字母是依序循环出现的。举个例子：

如果目标字母 target = 'z' 并且字符列表为 letters = ['a', 'b']，则答案返回 'a'
"""


class Solution:
    def nextGreatestLetter(self, letters, target: str) -> str:
        ascii_lower = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
        dict_letter = {}
        n = 0
        for i in range(len(ascii_lower)):
            dict_letter[i] = ascii_lower[i]
        for index in dict_letter.keys():
            if dict_letter[index] == target:
                n = index
                break
        for item in dict_letter:
            for letter in letters:
                if letter == dict_letter[item] and target != letter:
                    if item > n:
                        return letter


letters = ["c", "f", "j"]
target = "d"
sol = Solution()
res = sol.nextGreatestLetter(letters, target)
print(res)
