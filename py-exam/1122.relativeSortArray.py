#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你两个数组，arr1 和 arr2，

arr2 中的元素各不相同
arr2 中的每个元素都出现在 arr1 中
对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。
"""


class Solution:
    def relativeSortArray(self, arr1, arr2):
        arr1.sort()
        arr3 = []
        for a in arr2:
            for b in arr1[:]:
                if b == a:
                    arr3.append(b)
                    arr1.remove(b)

        return arr3 + arr1


arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
sol = Solution()
res = sol.relativeSortArray(arr1, arr2)
print(res)
