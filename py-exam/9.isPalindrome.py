#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
"""


class Solution:
    def isPalindrome(self, x):

        l1 = list(str(x))
        l1.reverse()
        s = ''.join(l1)
        if s == str(x):
            return True
        else:
            return False


n = 121
sol = Solution()
res = sol.isPalindrome(n)
print(res)
