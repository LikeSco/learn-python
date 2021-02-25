#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个字符串数组 words ，数组中的每个字符串都可以看作是一个单词。请你按 任意 顺序返回 words 中是其他单词的子字符串的所有单词。

如果你可以删除 words[j] 最左侧和/或最右侧的若干字符得到 word[i] ，那么字符串 words[i] 就是 words[j] 的一个子字符串。
"""


class Solution:
    def stringMatching(self, words):
        list_result = []
        s = '-'.join(words)
        for word in words:
            if s.count(word) > 1:
                list_result.append(word)

        return list_result


words = ["mass", "as", "hero", "superhero"]
sol = Solution()
res = sol.stringMatching(words)
print(res)
