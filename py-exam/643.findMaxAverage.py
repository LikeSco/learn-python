#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
"""


class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        sum1 = sum(nums[:k])
        result = sum1
        for i in range(1, len(nums) - k + 1):
            sum1 += nums[i + k - 1] - nums[i - 1]
            result = max(result, sum1)
        return result / k


nums = [1, 12, -5, -6, 50, 3]
k = 4
sol = Solution()
res = sol.findMaxAverage(nums, k)
print(res)
