#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num3 = int(num1) * int(num2)
        return str(num3)


num1 = "123"
num2 = "456"
sol = Solution()
res = sol.multiply(num1, num2)
print(res)
