#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个 m * n 的矩阵，矩阵中的数字 各不相同 。请你按 任意 顺序返回矩阵中的所有幸运数。

幸运数是指矩阵中满足同时下列两个条件的元素：

在同一行的所有元素中最小
在同一列的所有元素中最大
"""


class Solution:
    def luckyNumbers(self, matrix):
        list_num = []
        for arr in matrix:
            list_col = []
            num = min(arr)
            index = arr.index(num)
            for arr in matrix:
                list_col.append(arr[index])
            if num == max(list_col):
                list_num.append(num)

        return list_num


matrix = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]
sol = Solution()
res = sol.luckyNumbers(matrix)
print(res)
