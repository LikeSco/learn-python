#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。

现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。
"""


class Solution:
    def findLHS(self, nums) -> int:
        nums.sort()
        print(nums)
        result = 0
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                result = max(result, nums.count(nums[i]) + nums.count(nums[i + 1]))
        return result


nums = [1, 4, 1, 3, 1, -14, 1, -13]
sol = Solution()
res = sol.findLHS(nums)
print(res)
