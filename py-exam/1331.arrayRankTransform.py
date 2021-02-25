#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个整数数组 arr ，请你将数组中的每个元素替换为它们排序后的序号。

序号代表了一个元素有多大。序号编号的规则如下：

序号从 1 开始编号。
一个元素越大，那么序号越大。如果两个元素相等，那么它们的序号相同。
每个数字的序号都应该尽可能地小。
"""


class Solution:
    def arrayRankTransform(self, arr):
        list_num = []
        dict_arr = {}
        arr1 = list(set(arr))
        arr1.sort()
        for i, n in enumerate(arr1):
            dict_arr[n] = i + 1
        for item in arr:
            list_num.append(dict_arr[item])

        return list_num


arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
sol = Solution()
res = sol.arrayRankTransform(arr)
print(res)