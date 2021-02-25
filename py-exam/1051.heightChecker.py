#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
学校在拍年度纪念照时，一般要求学生按照 非递减 的高度顺序排列。

请你返回能让所有学生以 非递减 高度排列的最小必要移动人数。

注意，当一组学生被选中时，他们之间可以以任何可能的方式重新排序，而未被选中的学生应该保持不动。
"""


class Solution:
    def heightChecker(self, heights) -> int:
        dict_num = {}
        for i, n in enumerate(heights):
            dict_num[i] = n
        heights.sort()
        heights1 = list(dict_num.values())
        if heights == heights1:
            return 0
        i = 0
        result = 0
        while i < len(heights):
            if heights1[i] != heights[i]:
                result += 1
            i += 1
        return result


heights = [5, 1, 2, 3, 4]
sol = Solution()
res = sol.heightChecker(heights)
print(res)
