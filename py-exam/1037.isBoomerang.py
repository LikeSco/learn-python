#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
回旋镖定义为一组三个点，这些点各不相同且不在一条直线上。

给出平面上三个点组成的列表，判断这些点是否可以构成回旋镖。
"""


class Solution:
    def isBoomerang(self, points) -> bool:
        x1y1 = points[0]
        x2y2 = points[1]
        x3y3 = points[2]
        if x1y1 == x2y2 or x2y2 == x3y3 or x1y1 == x3y3:
            return False
        if (x2y2[0] - x1y1[0]) == 0:
            if x3y3[0] == x1y1[0]:
                return False
            else:
                return True
        a = (x2y2[1] - x1y1[1]) / (x2y2[0] - x1y1[0])
        b = x1y1[1] - (x1y1[0] * a)
        if a * x3y3[0] + b == x3y3[1]:
            return False
        return True


points = [[1, 1], [2, 3], [3, 2]]
sol = Solution()
res = sol.isBoomerang(points)
print(res)
