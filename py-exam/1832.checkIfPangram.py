#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
全字母句 指包含英语字母表中每个字母至少一次的句子。

给你一个仅由小写英文字母组成的字符串 sentence ，请你判断 sentence 是否为 全字母句 。

如果是，返回 true ；否则，返回 false 。
"""


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        chars = 'abcdefghijklmnopqrstuvwxyz'
        s = list(set(sentence))
        s.sort()
        if ''.join(s) == chars:
            return True
        return False


sentence = "thequickbrownfoxjumpsoverthelazydog"
sol = Solution()
res = sol.checkIfPangram(sentence)
print(res)
