#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        result = n / 2
        while result >= 1:
            if result == 1:
                return True
            result = result / 2
        return False


n = 1024
sol = Solution()
res = sol.isPowerOfTwo(n)
print(res)
