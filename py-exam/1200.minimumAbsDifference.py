#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你个整数数组 arr，其中每个元素都 不相同。

请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。
"""


class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        diff = abs(arr[-1] - arr[0])
        result = []
        for i in range(len(arr) - 1):
            if abs(arr[i + 1] - arr[i]) < diff:
                diff = abs(arr[i + 1] - arr[i])
                result = [[arr[i], arr[i + 1]]]
            elif abs(arr[i + 1] - arr[i]) == diff:
                result.append([arr[i], arr[i + 1]])
        result.sort()
        return result


arr = [3, 8, -10, 23, 19, -4, -14, 27]
sol = Solution()
res = sol.minimumAbsDifference(arr)
print(res)
