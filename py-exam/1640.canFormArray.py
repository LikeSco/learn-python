#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个整数数组 arr ，数组中的每个整数 互不相同 。另有一个由整数数组构成的数组 pieces，其中的整数也 互不相同 。请你以 任意顺序 连接 pieces 中的数组以形成 arr 。但是，不允许 对每个数组 pieces[i] 中的整数重新排序。

如果可以连接 pieces 中的数组形成 arr ，返回 true ；否则，返回 false 。
"""


class Solution:
    def canFormArray(self, arr, pieces) -> bool:
        result = []
        for i in arr:
            for j in pieces:
                if i == j[0]:
                    result += j
        if result == arr:
            return True
        return False


arr = [2, 82, 79, 95, 28]
pieces = [[2], [82], [28], [79, 95]]
sol = Solution()
res = sol.canFormArray(arr, pieces)
print(res)
