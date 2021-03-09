#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。

找到所有出现两次的元素。
"""


class Solution:
    def findDuplicates(self, nums):
        result = []
        d_n = {}
        if len(nums) != 0:
            for n in nums:
                if n not in d_n.keys():
                    d_n[n] = 1
                else:
                    result.append(n)
        return result


nums = [4, 3, 2, 7, 8, 2, 3, 1]
sol = Solution()
res = sol.findDuplicates(nums)
print(res)
