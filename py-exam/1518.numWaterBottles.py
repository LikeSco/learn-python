#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
小区便利店正在促销，用 numExchange 个空酒瓶可以兑换一瓶新酒。你购入了 numBottles 瓶酒。

如果喝掉了酒瓶中的酒，那么酒瓶就会变成空的。

请你计算 最多 能喝到多少瓶酒。
"""


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        sumCount = 0
        while numBottles >= numExchange:
            exchangeCount = numBottles // numExchange
            remainCount = numBottles % numExchange
            sumCount += exchangeCount * numExchange
            numBottles = exchangeCount + remainCount

        sumCount += numBottles
        return sumCount


numBottles = 15
numExchange = 4
sol = Solution()
res = sol.numWaterBottles(numBottles, numExchange)
print(res)
