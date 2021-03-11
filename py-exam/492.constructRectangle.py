#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math

"""
作为一位web开发者， 懂得怎样去规划一个页面的尺寸是很重要的。 现给定一个具体的矩形页面面积，你的任务是设计一个长度为 L 和宽度为 W 且满足以下要求的矩形的页面。要求：

1. 你设计的矩形页面必须等于给定的目标面积。

2. 宽度 W 不应大于长度 L，换言之，要求 L >= W 。

3. 长度 L 和宽度 W 之间的差距应当尽可能小。
你需要按顺序输出你设计的页面的长度 L 和宽度 W。
"""


class Solution:
    def constructRectangle(self, area: int):
        a = int(math.sqrt(area))
        if area == a * a:
            return [a, a]
        else:
            for i in range(a + 1, area + 1):
                j = area / i
                if j == int(j):
                    return [i, int(j)]


area = 999998
sol = Solution()
res = sol.constructRectangle(area)
print(res)
