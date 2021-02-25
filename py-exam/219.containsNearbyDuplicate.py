#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。
"""


class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        dict_num = {}
        for i in range(len(nums)):
            if nums[i] in dict_num and (i - dict_num[nums[i]]) <= k:
                return True
            else:
                dict_num[nums[i]] = i
        return False


nums = [1, 2, 3, 1, 2, 3]
k = 2
sol = Solution()
res = sol.containsNearbyDuplicate(nums, k)
print(res)
