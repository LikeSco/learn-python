#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。
"""


class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        for num in nums:
            if num >= target:
                return nums.index(num)

        return len(nums)


nums = [1, 3, 5, 6]
target = 7
sol = Solution()
res = sol.searchInsert(nums, target)
print(res)
