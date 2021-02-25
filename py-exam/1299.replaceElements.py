#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个数组 arr ，请你将每个元素用它右边最大的元素替换，如果是最后一个元素，用 -1 替换。

完成所有替换操作后，请你返回这个数组
"""


class Solution:
    def replaceElements(self, arr):
        list_n = []
        while len(arr) > 0:
            for n in arr[:]:
                if len(arr) == 1:
                    list_n.append(-1)
                    arr.remove(n)
                else:
                    arr.remove(n)
                    list_n.append(max(arr))
                    break

        return list_n


arr = [17, 18, 5, 4, 6, 1]
sol = Solution()
res = sol.replaceElements(arr)
print(res)
