#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。

对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。

你可以返回任何满足上述条件的数组作为答案。
"""


class Solution:
    def sortArrayByParityII(self, A):
        A1 = []
        A2 = []
        A3 = []
        for n in A:
            if n % 2 == 0:
                A1.append(n)
            else:
                A2.append(n)
        for i in range(len(A1)):
            A3.append(A1[i])
            A3.append(A2[i])
        return A3


A = [4, 2, 5, 7]
sol = Solution()
res = sol.sortArrayByParityII(A)
print(res)
