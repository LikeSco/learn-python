#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
在一个给定的数组nums中，总是存在一个最大元素 。

查找数组中的最大元素是否至少是数组中每个其他数字的两倍。

如果是，则返回最大元素的索引，否则返回-1。
"""


class Solution:
    def dominantIndex(self, nums) -> int:
        if len(nums) == 1:
            return 0
        max_num = max(nums)
        index = nums.index(max_num)
        nums.remove(max_num)
        second_max = max(nums)
        if max_num >= second_max * 2:
            return index
        return -1


nums = [1, 2, 3, 4]
sol = Solution()
res = sol.dominantIndex(nums)
print(res)
