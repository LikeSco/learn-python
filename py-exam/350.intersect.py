#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定两个数组，编写一个函数来计算它们的交集。
"""


class Solution:
    def intersect(self, nums1, nums2):
        nums3 = []
        for n1 in nums1:
            if n1 in nums2:
                nums3.append(n1)
                nums2.remove(n1)

        return nums3


nums1 = [1, 2, 2, 1]
nums2 = [2, 2, 3]
sol = Solution()
res = sol.intersect(nums1, nums2)
print(res)
