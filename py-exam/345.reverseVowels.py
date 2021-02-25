#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
"""
import re


class Solution:
    def reverseVowels(self, s: str) -> str:
        if s.strip() == '':
            return s
        pattern = 'aeiouAEIOU'
        s1 = re.sub('[^' + pattern + ']', '', s)
        l1 = list(s)
        l2 = list(s1)
        for i, ch in enumerate(l1):
            if ch in pattern:
                l1[i] = l2.pop()

        return ''.join(l1)


s = "hello"
sol = Solution()
res = sol.reverseVowels(s)
print(res)
