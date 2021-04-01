#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

"""
给你一个混合字符串 s ，请你返回 s 中 第二大 的数字，如果不存在第二大的数字，请你返回 -1 。

混合字符串 由小写英文字母和数字组成。
"""


class Solution:
    def secondHighest(self, s: str) -> int:
        nums = re.findall('[0-9]', s)
        nums = list(set(nums))
        if len(nums) == 1 or len(nums) == 0:
            return -1
        nums.sort()
        return int(nums[-2])


s = "dfa12321afd"
sol = Solution()
res = sol.secondHighest(s)
print(res)
