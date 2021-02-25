#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
"""


class Solution:
    def plusOne(self, digits):

        x = int(''.join(str(num) for num in digits))
        if x == 0:
            digits[-1] = 1
            return digits
        else:
            y = x + 1
            dict_result = list(map(int, list(str(y))))
            return dict_result


digits = [4, 3, 2, 1]
sol = Solution()
res = sol.plusOne(digits)
print(res)
