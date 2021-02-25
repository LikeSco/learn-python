#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s1 = re.sub('[^a-z^0-9]', '', s)
        l1 = list(s1)
        l1.reverse()
        s2 = ''.join(l1)
        if s1 == s2:
            return True
        else:
            return False


s = 'A man, a plan, a canal: Panama'
sol = Solution()
res = sol.isPalindrome(s)
print(res)
