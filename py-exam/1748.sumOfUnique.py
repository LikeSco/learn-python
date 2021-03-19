#!/usr/bin/python
# -*- coding: UTF-8 -*-
from collections import Counter

"""
给你一个整数数组 nums 。数组中唯一元素是那些只出现 恰好一次 的元素。

请你返回 nums 中唯一元素的 和 。
"""


class Solution:
    def sumOfUnique(self, nums) -> int:
        a = Counter(nums)
        result = []
        for item in a.keys():
            if a[item] == 1:
                result.append(item)

        return sum(result)


nums = [1, 2, 3, 2]
sol = Solution()
res = sol.sumOfUnique(nums)
print(res)
