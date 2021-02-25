#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
"""


class Solution:
    def missingNumber(self, nums) -> int:
        n = len(nums)
        nums1 = []
        for i in range(n + 1):
            nums1.append(i)
        return set(nums1).difference(set(nums)).pop()


nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
sol = Solution()
res = sol.missingNumber(nums)
print(res)
