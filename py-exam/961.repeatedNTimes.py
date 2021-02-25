#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
在大小为 2N 的数组 A 中有 N+1 个不同的元素，其中有一个元素重复了 N 次。

返回重复了 N 次的那个元素。
"""


class Solution:
    def repeatedNTimes(self, A) -> int:
        n_count = len(A) / 2
        for n in A:
            if A.count(n) == n_count:
                return n


A = [2, 1, 2, 5, 3, 2]
sol = Solution()
res = sol.repeatedNTimes(A)
print(res)
