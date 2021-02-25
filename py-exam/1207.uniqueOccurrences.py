#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。

如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。
"""


class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        arr1 = list(set(arr))
        list_count = []
        for n in arr1:
            list_count.append(arr.count(n))
        list_count1 = list(set(list_count))
        list_count.sort()
        list_count1.sort()
        if list_count1 == list_count:
            return True
        return False


arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
sol = Solution()
res = sol.uniqueOccurrences(arr)
print(res)
