#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
"""


class Solution:
    def singleNumber(self, nums) -> int:
        for num in nums:
            if nums.count(num) == 1:
                return num


nums = [4, 1, 2, 1, 2]
sol = Solution()
res = sol.singleNumber(nums)
print(res)
