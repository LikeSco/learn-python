#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个整数数组 arr ，以及 a、b 、c 三个整数。请你统计其中好三元组的数量。

如果三元组 (arr[i], arr[j], arr[k]) 满足下列全部条件，则认为它是一个 好三元组 。

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
其中 |x| 表示 x 的绝对值。

返回 好三元组的数量 。
"""


class Solution:
    def countGoodTriplets(self, arr, a: int, b: int, c: int):
        result = []
        for i in range(len(arr) - 2):
            for j in range(1, len(arr) - 1):
                for k in range(2, len(arr)):
                    if i < j < k:
                        if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            result.append((arr[i], arr[j], arr[k]))

        return len(result)


arr = [3, 0, 1, 1, 9, 7]
a = 7
b = 2
c = 3
sol = Solution()
res = sol.countGoodTriplets(arr, a, b, c)
print(res)
