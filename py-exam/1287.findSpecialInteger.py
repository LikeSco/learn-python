#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个非递减的 有序 整数数组，已知这个数组中恰好有一个整数，它的出现次数超过数组元素总数的 25%。

请你找到并返回这个整数
"""


class Solution:
    def findSpecialInteger(self, arr) -> int:
        for n in arr:
            if arr.count(n) > len(arr) / 4:
                return n


arr = [1, 2, 2, 6, 6, 6, 6, 7, 10]
sol = Solution()
res = sol.findSpecialInteger(arr)
print(res)
