#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一副牌，每张牌上都写着一个整数。

此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：

每组都有 X 张牌。
组内所有的牌上都写着相同的整数。
仅当你可选的 X >= 2 时返回 true。
"""


class Solution:
    def hasGroupsSizeX(self, deck) -> bool:
        deck1 = set(deck)
        list_count = []
        for n in deck1:
            list_count.append(deck.count(n))
        min_count = min(list_count)
        if min_count < 2:
            return False
        i = 2
        while i <= min_count:
            for j in range(len(list_count)):
                if list_count[j] % i != 0:
                    i += 1
                    break
                if j == len(list_count) - 1:
                    return True
        return False


deck = [1, 1, 1, 2, 2, 2, 3, 3]
sol = Solution()
res = sol.hasGroupsSizeX(deck)
print(res)
