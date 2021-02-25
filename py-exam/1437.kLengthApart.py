#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个由若干 0 和 1 组成的数组 nums 以及整数 k。如果所有 1 都至少相隔 k 个元素，则返回 True ；否则，返回 False 。
"""


class Solution:
    def kLengthApart(self, nums, k):
        num = ''.join(str(n) for n in nums)
        index = 0
        result = -k - 2
        while index < len(num):
            index = num.find('1', index)
            if index == -1:
                break
            if index - result > k:
                result = index
                index += 1
            else:
                return False

        return True


nums = [1, 0, 0, 0, 1, 0, 0, 1]
k = 2
sol = Solution()
res = sol.kLengthApart(nums, k)
print(res)
