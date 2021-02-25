#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个偶数长度的数组，其中不同的数字代表着不同种类的糖果，每一个数字代表一个糖果。你需要把这些糖果平均分给一个弟弟和一个妹妹。返回妹妹可以获得的最大糖果的种类数
"""


class Solution:
    def distributeCandies(self, candyType) -> int:
        count = int(len(candyType) / 2)
        candies = set(candyType)
        count1 = len(candies)
        if count1 >= count:
            return count
        else:
            return count1


candyType = [1, 1, 2, 2, 3, 3, 1, 1]
sol = Solution()
res = sol.distributeCandies(candyType)
print(res)
