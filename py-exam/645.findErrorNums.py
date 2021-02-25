#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
集合 s 包含从 1 到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合 丢失了一个数字 并且 有一个数字重复 。

给定一个数组 nums 代表了集合 S 发生错误后的结果。

请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。
"""


class Solution:
    def findErrorNums(self, nums):
        nums1 = list(range(1, len(nums) + 1))
        nums2 = set(nums)
        a = sum(nums) - sum(nums2)
        b = sum(nums1) - sum(nums2)

        return [a, b]


nums = [1, 2, 2, 4]
sol = Solution()
res = sol.findErrorNums(nums)
print(res)
