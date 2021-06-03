#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
小朋友 A 在和 ta 的小伙伴们玩传信息游戏，游戏规则如下：

有 n 名玩家，所有玩家编号分别为 0 ～ n-1，其中小朋友 A 的编号为 0
每个玩家都有固定的若干个可传信息的其他玩家（也可能没有）。传信息的关系是单向的（比如 A 可以向 B 传信息，但 B 不能向 A 传信息）。
每轮信息必须需要传递给另一个人，且信息可重复经过同一个人
给定总玩家数 n，以及按 [玩家编号,对应可传递玩家编号] 关系组成的二维数组 relation。返回信息从小 A (编号 0 ) 经过 k 轮传递到编号为 n-1 的小伙伴处的方案数；若不能到达，返回 0。
"""


class Solution:
    def numWays(self, n: int, relation, k: int) -> int:
        d = {k: [] for k in range(n)}
        for r in relation:
            a, b = r
            d[a].append(b)
        reachable = [0]
        for i in range(k):
            reachable = sum((d[k] for k in reachable), [])
        return reachable.count(n - 1)


n = 5
relation = [[0, 2], [2, 1], [3, 4], [2, 3], [1, 4], [2, 0], [0, 4]]
k = 3
sol = Solution()
res = sol.numWays(n, relation, k)
print(res)
