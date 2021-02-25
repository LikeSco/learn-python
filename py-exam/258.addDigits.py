#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。
"""


class Solution:
    def addDigits(self, num: int) -> int:
        nums = list(str(num))
        while len(nums) > 1:
            result = 0
            for n in nums:
                result += int(n)
            nums = list(str(result))
        return int(nums[0])


num = 38
sol = Solution()
res = sol.addDigits(num)
print(res)
