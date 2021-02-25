#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个整数数组 nums，请你返回其中位数为 偶数 的数字的个数。
"""


class Solution:
    def findNumbers(self, nums) -> int:
        count = 0
        for num in nums:
            s = str(num)
            if len(s) % 2 == 0:
                count += 1

        return count


nums = [12, 345, 2, 6, 7896]
sol = Solution()
res = sol.findNumbers(nums)
print(res)
