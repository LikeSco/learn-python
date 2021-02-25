#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个整数数组 A，我们只能用以下方法修改该数组：我们选择某个索引 i 并将 A[i] 替换为 -A[i]，然后总共重复这个过程 K 次。（我们可以多次选择同一个索引 i。）

以这种方式修改数组后，返回数组可能的最大和。
"""


class Solution:
    def largestSumAfterKNegations(self, A, K: int) -> int:
        count = 0
        while count < K:
            min_a = min(A)
            index = A.index(min_a)
            A[index] = -A[index]
            count += 1

        return sum(A)


A = [3, -1, 0, 2]
K = 3
sol = Solution()
res = sol.largestSumAfterKNegations(A, K)
print(res)
