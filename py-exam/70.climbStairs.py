#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        regulation = {1: 1, 2: 2}
        i = 3
        while i <= n:
            nums = list(regulation.values())
            result = nums[-2] + nums[-1]
            regulation[i] = result
            i += 1
        return regulation[n]


n = 11
sol = Solution()
res = sol.climbStairs(n)
print(res)
