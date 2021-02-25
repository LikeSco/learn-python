#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个非负整数数组 A，返回一个数组，在该数组中， A 的所有偶数元素之后跟着所有奇数元素。

你可以返回满足此条件的任何数组作为答案。
"""


class Solution:
    def sortArrayByParity(self, A):
        A1 = []
        A2 = []
        for n in A:
            if n % 2 == 0:
                A1.append(n)
            else:
                A2.append(n)
        return A1 + A2


A = [3, 1, 2, 4]
sol = Solution()
res = sol.sortArrayByParity(A)
print(res)
