#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定两个数组，编写一个函数来计算它们的交集。
"""


class Solution:
    def intersection(self, nums1, nums2):
        nums3 = list(set(nums1).difference(nums2))
        nums4 = list(set(nums1).difference(nums3))
        return nums4


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
sol = Solution()
res = sol.intersection(nums1, nums2)
print(res)
