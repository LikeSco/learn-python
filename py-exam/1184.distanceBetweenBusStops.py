#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
环形公交路线上有 n 个站，按次序从 0 到 n - 1 进行编号。我们已知每一对相邻公交站之间的距离，distance[i] 表示编号为 i 的车站和编号为 (i + 1) % n 的车站之间的距离。

环线上的公交车都可以按顺时针和逆时针的方向行驶。

返回乘客从出发点 start 到目的地 destination 之间的最短距离。
"""


class Solution:
    def distanceBetweenBusStops(self, distance, start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        pos_dis = sum(distance[start:destination])
        neg_dis = sum(distance) - pos_dis
        return min(pos_dis, neg_dis)


distance = [1, 2, 3, 4]
start = 0
destination = 2
sol = Solution()
res = sol.distanceBetweenBusStops(distance, start, destination)
print(res)
