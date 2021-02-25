#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个段落 (paragraph) 和一个禁用单词列表 (banned)。返回出现次数最多，同时不在禁用列表中的单词。

题目保证至少有一个词不在禁用列表中，而且答案唯一。

禁用列表中的单词用小写字母表示，不含标点符号。段落中的单词不区分大小写。答案都是小写字母。
"""
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub('[^ a-z]', ' ', paragraph)
        arr = paragraph.split(' ')
        count = 0
        result = ''
        for item in set(arr):
            if item != '':
                if item not in banned:
                    if arr.count(item) > count:
                        count = arr.count(item)
                        result = item
        return result


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
sol = Solution()
res = sol.mostCommonWord(paragraph, banned)
print(res)
