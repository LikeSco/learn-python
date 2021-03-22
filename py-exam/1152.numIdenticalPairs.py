#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个整数数组 nums 。

如果一组数字 (i,j) 满足 nums[i] == nums[j] 且 i < j ，就可以认为这是一组 好数对 。

返回好数对的数目。
"""


class Solution:
    def numIdenticalPairs(self, nums) -> int:
        result = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i < j:
                    if nums[i] == nums[j]:
                        result.append((i, j))

        return len(result)


nums = [1, 2, 3, 1, 1, 3]
sol = Solution()
res = sol.numIdenticalPairs(nums)
print(res)
