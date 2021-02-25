#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
在一个小镇里，按从 1 到 N 标记了 N 个人。传言称，这些人中有一个是小镇上的秘密法官。

如果小镇的法官真的存在，那么：

小镇的法官不相信任何人。
每个人（除了小镇法官外）都信任小镇的法官。
只有一个人同时满足属性 1 和属性 2 。
给定数组 trust，该数组由信任对 trust[i] = [a, b] 组成，表示标记为 a 的人信任标记为 b 的人。

如果小镇存在秘密法官并且可以确定他的身份，请返回该法官的标记。否则，返回 -1。
"""


class Solution:
    def findJudge(self, N: int, trust) -> int:
        if N == 1 and len(trust) == 0:
            return 1
        trust1 = []
        trust2 = []
        for item in trust:
            trust1.append(item[1])
            trust2.append(item[0])

        for item1 in trust1:
            if trust1.count(item1) == N - 1:
                if item1 not in trust2:
                    return item1
        return -1


N = 4
trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
sol = Solution()
res = sol.findJudge(N, trust)
print(res)
