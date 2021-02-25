#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个 严格升序排列 的正整数数组 arr 和一个整数 k 。

请你找到这个数组里第 k 个缺失的正整数。
"""


class Solution:
    def findKthPositive(self, arr, k: int) -> int:
        list_nums = []
        i = 1
        while i <= max(arr) + k:
            list_nums.append(i)
            i += 1
        count = 0
        for n in list_nums:
            if n not in arr:
                count += 1
            if count == k:
                return n


arr = [2, 3, 4, 7, 11]
k = 5
sol = Solution()
res = sol.findKthPositive(arr, k)
print(res)
