#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
在整数数组中，如果一个整数的出现频次和它的数值大小相等，我们就称这个整数为「幸运数」。

给你一个整数数组 arr，请你从中找出并返回一个幸运数。

如果数组中存在多个幸运数，只需返回 最大 的那个。
如果数组中不含幸运数，则返回 -1 。
"""


class Solution:
    def findLucky(self, arr) -> int:
        list_lucky = []
        for n in arr:
            if n not in list_lucky:
                if n == arr.count(n):
                    list_lucky.append(n)

        if len(list_lucky) == 0:
            return -1

        return max(list_lucky)


arr = [1, 2, 2, 3, 3, 3]
sol = Solution()
res = sol.findLucky(arr)
print(res)
