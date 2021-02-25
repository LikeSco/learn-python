#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。

水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。

反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]
"""


class Solution:
    def flipAndInvertImage(self, A):
        for item in A:
            item.reverse()
            for i in range(len(item)):
                if item[i] == 0:
                    item[i] = 1
                elif item[i] == 1:
                    item[i] = 0
        return A


A = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
sol = Solution()
res = sol.flipAndInvertImage(A)
print(res)
