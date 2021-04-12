#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
"""
import math


class Solution:
    def mySqrt(self, x: int) -> int:
        n = math.pow(x, 0.5)
        return int(n)


x = 8
sol = Solution()
res = sol.mySqrt(x)
print(res)
