#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个长度固定的整数数组 arr，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。

注意：请不要在超过该数组长度的位置写入元素。

要求：请对输入的数组 就地 进行上述修改，不要从函数返回任何东西。
"""


class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        length = len(arr)
        i = 0
        while i < length:
            if arr[i] == 0:
                arr.insert(i + 1, 0)
                i += 1
            i += 1
        while len(arr) != length:
            arr.pop()
        return arr


arr = [1, 0, 2, 3, 0, 4, 5, 0]
sol = Solution()
res = sol.duplicateZeros(arr)
print(res)
