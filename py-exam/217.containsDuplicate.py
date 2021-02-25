#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个整数数组，判断是否存在重复元素。

如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
"""


class Solution:
    def containsDuplicate(self, nums) -> bool:
        nums1 = list(set(nums))
        if len(nums1) < len(nums):
            return True
        else:
            return False


nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
sol = Solution()
res = sol.containsDuplicate(nums)
print(res)
