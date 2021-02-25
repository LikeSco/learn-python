#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个字符串牌照 licensePlate 和一个字符串数组 words ，请你找出并返回 words 中的 最短补全词 。

如果单词列表（words）中的一个单词包含牌照（licensePlate）中所有的字母，那么我们称之为 补全词 。在所有完整词中，最短的单词我们称之为 最短补全词 。

单词在匹配牌照中的字母时要：

忽略牌照中的数字和空格。
不区分大小写，比如牌照中的 "P" 依然可以匹配单词中的 "p" 字母。
如果某个字母在牌照中出现不止一次，那么该字母在补全词中的出现次数应当一致或者更多。
例如：licensePlate = "aBc 12c"，那么它由字母 'a'、'b' （忽略大写）和两个 'c' 。可能的 补全词 是 "abccdef"、"caaacab" 以及 "cbca" 。

题目数据保证一定存在一个最短补全词。当有多个单词都符合最短补全词的匹配条件时取单词列表中最靠前的一个。
"""
import re


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words) -> str:
        licensePlate = licensePlate.lower()
        s = re.sub('[^a-z]', '', licensePlate)
        result = ''.join(words)
        for item in words:
            flag = True
            list_item = list(item)
            for ch in s:
                if ch not in list_item:
                    flag = False
                    break
                else:
                    list_item.remove(ch)
            if flag:
                if len(item) < len(result):
                    result = item
        return result


licensePlate = "Ah71752"
words = ["suggest", "letter", "of", "husband", "easy", "education", "drug", "prevent", "writer", "old"]
sol = Solution()
res = sol.shortestCompletingWord(licensePlate, words)
print(res)
