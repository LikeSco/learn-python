#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
有一堆石头，每块石头的重量都是正整数。

每一回合，从中选出两块 最重的 石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。
"""


class Solution:
    def lastStoneWeight(self, stones) -> int:
        while len(stones) >= 2:
            y = max(stones)
            stones.remove(y)
            x = max(stones)
            stones.remove(x)
            if x != y:
                stones.append(y - x)
        if len(stones) == 0:
            return 0
        return stones[0]


stones = [2, 7, 4, 1, 8, 1]
sol = Solution()
res = sol.lastStoneWeight(stones)
print(res)
