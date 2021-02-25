#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个由不同字符组成的字符串 allowed 和一个字符串数组 words 。如果一个字符串的每一个字符都在 allowed 中，就称这个字符串是 一致字符串 。

请你返回 words 数组中 一致字符串 的数目。
"""


class Solution:
    def countConsistentStrings(self, allowed: str, words) -> int:
        count = 0
        for item in words:
            flag = True
            for ch in set(list(item)):
                if ch not in allowed:
                    flag = False
                    break
            if flag:
                count += 1
        return count


allowed = "ab"
words = ["ad", "bd", "aaab", "baa", "badab"]
sol = Solution()
res = sol.countConsistentStrings(allowed, words)
print(res)
