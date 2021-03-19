#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个整数数组 nums ，请你将数组按照每个值的频率 升序 排序。如果有多个值的频率相同，请你按照数值本身将它们 降序 排序。

请你返回排序后的数组。
"""
from collections import Counter


class Solution:
    def frequencySort(self, nums):
        result = []
        c_nums = Counter(nums)
        key_nums = list(c_nums.keys())
        key_nums.sort()
        key_nums.reverse()
        while len(key_nums) != 0:
            min_num = min(key_nums, key=(lambda k: c_nums[k]))
            count = c_nums[min_num]
            for i in range(count):
                result.append(min_num)
            del c_nums[min_num]
            key_nums.remove(min_num)
        return result


nums = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
sol = Solution()
res = sol.frequencySort(nums)
print(res)
