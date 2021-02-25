#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
"""


class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for n in nums[:]:
            if n == 0:
                nums.remove(n)
                count += 1
        for i in range(count):
            nums.append(0)
