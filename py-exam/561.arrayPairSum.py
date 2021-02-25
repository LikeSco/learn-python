#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定长度为 2n 的整数数组 nums ，你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从 1 到 n 的 min(ai, bi) 总和最大。

返回该 最大总和 。
"""


class Solution:
    def arrayPairSum(self, nums) -> int:
        list_min = []
        nums.sort()
        for i in range(len(nums)):
            if i % 2 == 0:
                list_min.append(nums[i])
        return sum(list_min)


nums = [6, 2, 6, 5, 1, 2]
sol = Solution()
res = sol.arrayPairSum(nums)
print(res)
