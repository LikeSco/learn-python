#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。
"""


class Solution:
    def majorityElement(self, nums) -> int:
        nums1 = set(nums)
        n = len(nums) / 2
        for num in nums1:
            if nums.count(num) > n:
                return num


nums = [2, 2, 1, 1, 1, 2, 2]
sol = Solution()
res = sol.majorityElement(nums)
print(res)
