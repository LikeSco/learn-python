#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个整数数组 arr，请你检查是否存在两个整数 N 和 M，满足 N 是 M 的两倍（即，N = 2 * M）。

更正式地，检查是否存在两个下标 i 和 j 满足：

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
"""


class Solution:
    def checkIfExist(self, arr) -> bool:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j:
                    if arr[i] == arr[j] * 2 or arr[j] == arr[i] * 2:
                        return True

        return False


arr = [7, 1, 12, 11, 24]
sol = Solution()
res = sol.checkIfExist(arr)
print(res)
