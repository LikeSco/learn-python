#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
"""


class Solution:
    def merge(self, nums1, m: int, nums2, n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = 0
        i = len(nums1)
        while a == 0 and len(nums1) > 0:
            a = nums1.pop()
            if a == 0:
                pass
            else:
                nums1.append(a)

        for num in nums2:
            nums1.append(num)
        nums1.sort()

        j = len(nums1)
        while j < i:
            nums1.append(0)
            j += 1

        return nums1


nums1 = [-1, -1, 0, 0, 0, 0]
m = 4
nums2 = [-1, 0]
n = 2
sol = Solution()
res = sol.merge(nums1, m, nums2, n)
print(res)
