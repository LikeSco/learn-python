#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个整数数组 arr，请你判断数组中是否存在连续三个元素都是奇数的情况：如果存在，请返回 true ；否则，返回 false 。
"""


class Solution:
    def threeConsecutiveOdds(self, arr) -> bool:
        if len(arr) < 3:
            return False
        for i in range(len(arr) - 2):
            if arr[i] % 2 == 1 and arr[i + 1] % 2 == 1 and arr[i + 2] % 2 == 1:
                return True
        return False


arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]
sol = Solution()
res = sol.threeConsecutiveOdds(arr)
print(res)
