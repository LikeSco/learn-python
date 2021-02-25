#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
对于非负整数 X 而言，X 的数组形式是每位数字按从左到右的顺序形成的数组。例如，如果 X = 1231，那么其数组形式为 [1,2,3,1]。

给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式。
"""


class Solution:
    def addToArrayForm(self, A, K: int):
        x = ''.join(str(a) for a in A)
        y = int(x) + K
        result = list(str(y))
        result = [int(b) for b in result]
        return result


A = [2, 1, 5]
K = 806
sol = Solution()
res = sol.addToArrayForm(A, K)
print(res)
