#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个数组 nums ，数组中有 2n 个元素，按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列。

请你将数组按 [x1,y1,x2,y2,...,xn,yn] 格式重新排列，返回重排后的数组。
"""


class Solution:
    def shuffle(self, nums, n: int):
        nums1 = nums[0:n]
        nums2 = nums[n:]
        result = []
        for i in range(n):
            result.append(nums1[i])
            result.append(nums2[i])
        return result


nums = [2,5,1,3,4,7]
n = 3
sol = Solution()
res = sol.shuffle(nums, n)
print(res)