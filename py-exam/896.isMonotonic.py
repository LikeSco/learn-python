#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
如果数组是单调递增或单调递减的，那么它是单调的。

如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。

当给定的数组 A 是单调数组时返回 true，否则返回 false。
"""


class Solution:
    def isMonotonic(self, A) -> bool:
        dict_A = {}
        for i, n in enumerate(A):
            dict_A[i] = n
        A.sort()
        if list(dict_A.values()) == A:
            return True
        A.reverse()
        if list(dict_A.values()) == A:
            return True
        return False


A = [6, 5, 4, 4]
sol = Solution()
res = sol.isMonotonic(A)
print(res)
