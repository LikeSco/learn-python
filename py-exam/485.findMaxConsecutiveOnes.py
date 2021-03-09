#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个二进制数组， 计算其中最大连续 1 的个数。
"""


# noinspection PyTypeChecker
class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        list_n = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                if i == len(nums) - 1:
                    list_n.append(count)
            else:
                list_n.append(count)
                count = 0

        return max(list_n)


nums = [1, 1, 0, 1, 1, 1]
sol = Solution()
res = sol.findMaxConsecutiveOnes(nums)
print(res)
