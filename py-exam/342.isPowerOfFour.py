#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。

整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4x
"""


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        result = n / 4
        while result >= 1:
            if result == 1:
                return True
            result = result / 4
        return False


n = 64
sol = Solution()
res = sol.isPowerOfFour(n)
print(res)
