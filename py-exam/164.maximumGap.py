#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。

如果数组元素个数小于 2，则返回 0。
"""


class Solution:
    def maximumGap(self, nums) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        gap = 0
        for i in range(len(nums) - 1):
            if (nums[i + 1] - nums[i]) >= gap:
                gap = nums[i + 1] - nums[i]
        return gap


nums = [3, 6, 9, 1]
sol = Solution()
res = sol.maximumGap(nums)
print(res)
