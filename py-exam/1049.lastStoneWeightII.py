#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
有一堆石头，每块石头的重量都是正整数。

每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块石头。返回此石头最小的可能重量。如果没有石头剩下，就返回 0。
"""


class Solution:
    def lastStoneWeightII(self, stones) -> int:
        target = sum(stones) / 2.0
        candidates = {0}
        for x in stones:
            addition = set()
            for y in candidates:
                s = x + y
                if s == target:
                    return 0
                elif x + y < target:
                    addition.add(s)
            candidates = candidates.union(addition)
        return int(2 * (target - max(candidates)))


stones = [3, 3, 6, 4, 8, 8]
sol = Solution()
res = sol.lastStoneWeightII(stones)
print(res)
