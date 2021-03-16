#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个整数 n，请你每隔三位添加点（即 "." 符号）作为千位分隔符，并将结果以字符串格式返回。
"""


class Solution:
    def thousandSeparator(self, n: int) -> str:
        m = str(n)
        if len(m) <= 3:
            return m
        list_n = list(m)
        list_n.reverse()
        count = 1
        for i in range(len(list_n)):
            if count == 3 and i != len(list_n) - 1:
                list_n[i] = list_n[i] + '.'
                count = 1
            else:
                count += 1
        s = ''.join(list_n)
        list_s = list(s)
        list_s.reverse()
        return ''.join(list_s)


n = 1234567896
sol = Solution()
res = sol.thousandSeparator(n)
print(res)
