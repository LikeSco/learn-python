#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个偶数长度的字符串 s 。将其拆分成长度相同的两半，前一半为 a ，后一半为 b 。

两个字符串 相似 的前提是它们都含有相同数目的元音（'a'，'e'，'i'，'o'，'u'，'A'，'E'，'I'，'O'，'U'）。注意，s 可能同时含有大写和小写字母。

如果 a 和 b 相似，返回 true ；否则，返回 false 。
"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        chs = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        length = int(len(s) / 2)
        s1 = s[0:length]
        s2 = s[length:]
        count1 = 0
        count2 = 0
        for i in range(length):
            if s1[i] in chs:
                count1 += 1
            if s2[i] in chs:
                count2 += 1
        if count1 == count2:
            return True
        return False


s = "AbCdEfGh"
sol = Solution()
res = sol.halvesAreAlike(s)
print(res)
