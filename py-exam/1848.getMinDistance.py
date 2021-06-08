#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个整数数组 nums （下标 从 0 开始 计数）以及两个整数 target 和 start ，请你找出一个下标 i ，满足 nums[i] == target 且 abs(i - start) 最小化 。注意：abs(x) 表示 x 的绝对值。

返回 abs(i - start) 。

题目数据保证 target 存在于 nums 中。
"""


class Solution:
    def getMinDistance(self, nums, target: int, start: int) -> int:
        results = []
        for i in range(len(nums)):
            if nums[i] == target:
                if abs(i - start) == 0:
                    return 0
                results.append(abs(i - start))
        return min(results)


nums = [1, 2, 3, 4, 5]
target = 5
start = 3
sol = Solution()
res = sol.getMinDistance(nums, target, start)
print(res)
