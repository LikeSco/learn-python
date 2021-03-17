#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
桌上有 n 堆力扣币，每堆的数量保存在数组 coins 中。我们每次可以选择任意一堆，拿走其中的一枚或者两枚，求拿完所有力扣币的最少次数。
"""


class Solution:
    def minCount(self, coins) -> int:
        count = 0
        for coin in coins:
            if coin % 2 == 0:
                count += coin / 2
            else:
                count += (coin - 1) / 2 + 1
        return int(count)


coins = [2, 3, 10]
sol = Solution()
res = sol.minCount(coins)
print(res)
