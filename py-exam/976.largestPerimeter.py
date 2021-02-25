#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。

如果不能形成任何面积不为零的三角形，返回 0。
"""


class Solution:
    def largestPerimeter(self, A) -> int:
        A.sort()
        while len(A) >= 3:
            if A[-3] + A[-2] > A[-1]:
                return A[-3] + A[-2] + A[-1]
            A.pop()
        return 0


A = [3, 6, 2, 3]
sol = Solution()
res = sol.largestPerimeter(A)
print(res)
