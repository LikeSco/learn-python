#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个非负整数数组 nums 。如果存在一个数 x ，使得 nums 中恰好有 x 个元素 大于或者等于 x ，那么就称 nums 是一个 特殊数组 ，而 x 是该数组的 特征值 。

注意： x 不必 是 nums 的中的元素。

如果数组 nums 是一个 特殊数组 ，请返回它的特征值 x 。否则，返回 -1 。可以证明的是，如果 nums 是特殊数组，那么其特征值 x 是 唯一的 。
"""


class Solution:
    def specialArray(self, nums) -> int:
        nums.sort()
        x = 0
        count = 0
        result = []
        while x <= len(nums):
            for item in nums:
                if item >= x:
                    count += 1
                if count > x:
                    break
            if count == x:
                result.append(x)
            x += 1
            count = 0
        if len(result) != 1:
            return -1
        return result[0]


nums = [0, 4, 3, 0, 4]
sol = Solution()
res = sol.specialArray(nums)
print(res)
