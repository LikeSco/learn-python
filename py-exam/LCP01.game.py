#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
小A 和 小B 在玩猜数字。小B 每次从 1, 2, 3 中随机选择一个，小A 每次也从 1, 2, 3 中选择一个猜。他们一共进行三次这个游戏，请返回 小A 猜对了几次？

输入的guess数组为 小A 每次的猜测，answer数组为 小B 每次的选择。guess和answer的长度都等于3。
"""


class Solution:
    def game(self, guess, answer) -> int:
        count = 0
        for i in range(len(answer)):
            if guess[i] == answer[i]:
                count += 1
        return count


guess = [2, 2, 3]
answer = [3, 2, 1]
sol = Solution()
res = sol.game(guess, answer)
print(res)
