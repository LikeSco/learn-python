#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个仅由数字 6 和 9 组成的正整数 num。

你最多只能翻转一位数字，将 6 变成 9，或者把 9 变成 6 。

请返回你可以得到的最大数字。
"""


class Solution:
    def maximum69Number(self, num: int) -> int:
        list_num = list(str(num))
        for i in range(len(list_num)):
            if list_num[i] != '9':
                list_num[i] = '9'
                break
        return int(''.join(list_num))


num = 9669
sol = Solution()
res = sol.maximum69Number(num)
print(res)
