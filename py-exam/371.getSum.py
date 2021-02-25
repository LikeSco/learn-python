#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:

        return sum([a, b])


a = -2
b = 3
sol = Solution()
res = sol.getSum(a, b)
print(res)
