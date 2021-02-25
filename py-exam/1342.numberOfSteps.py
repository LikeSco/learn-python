#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个非负整数 num ，请你返回将它变成 0 所需要的步数。 如果当前数字是偶数，你需要把它除以 2 ；否则，减去 1 。
"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        while num != 0:
            if num % 2 == 0:
                num = num / 2
            else:
                num = num - 1
            step += 1
        return step


num = 29
sol = Solution()
res = sol.numberOfSteps(num)
print(res)
