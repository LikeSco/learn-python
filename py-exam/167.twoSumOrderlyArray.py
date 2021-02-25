#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个已按照升序排列的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
"""


class Solution:
    def twoSum(self, numbers, target: int):
        result = []
        val = {}
        i = 1
        val1 = {}
        j = 1
        for item in numbers:
            val[i] = item
            i += 1

        for num in numbers:
            while numbers.count(num) >= 3:
                numbers.remove(num)

        for item1 in numbers:
            val1[j] = item1
            j += 1

        for a in val1.keys():
            if len(result) == 0:
                for b in val1.keys():
                    if len(result) == 0:
                        if a != b:
                            if target == val1[a] + val1[b]:
                                for c in val.keys():
                                    if val[c] == val1[a]:
                                        result.append(c)
                                    if val[c] == val1[b]:
                                        result.append(c)

        dict_result = list(set(result))
        dict_result.sort()
        return dict_result


nums = [0, 0, 3, 4]
target = 0
sol = Solution()
res = sol.twoSum(nums, target)
print(res)
