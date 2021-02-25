#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给你一个整数数组  flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n ，能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false。
"""


class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        if len(flowerbed) == 1:
            if flowerbed[0] == 0 and n <= 1:
                return True
            elif flowerbed[0] == 1 and n == 0:
                return True
            else:
                return False
        while n > 0:
            for i in range(len(flowerbed)):
                if i == 0:
                    if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        n -= 1
                elif i == len(flowerbed) - 1:
                    if flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                        flowerbed[i] = 1
                        n -= 1
                else:
                    if flowerbed[i] == 0 and flowerbed[i + 1] == 0 and flowerbed[i - 1] == 0:
                        flowerbed[i] = 1
                        n -= 1
                if n == 0:
                    break
            if n > 0:
                return False
        return True


flowerbed = [1, 0, 0, 0, 1, 0, 0]
n = 2
sol = Solution()
res = sol.canPlaceFlowers(flowerbed, n)
print(res)
