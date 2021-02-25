#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。

换而言之，对于每个 nums[i] 你必须计算出有效的 j 的数量，其中 j 满足 j != i 且 nums[j] < nums[i] 。

以数组形式返回答案。
"""


class Solution:
    def smallerNumbersThanCurrent(self, nums):
        list_n = []
        for n in nums:
            i = 0
            count = 0
            for i in range(i, len(nums)):
                if nums[i] < n:
                    count += 1
            list_n.append(count)

        return list_n


nums = [8, 1, 2, 2, 3]
sol = Solution()
res = sol.smallerNumbersThanCurrent(nums)
print(res)
