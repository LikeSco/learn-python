#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。

如果 n 是快乐数就返回 True ；不是，则返回 False 。
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        unhappy = set()
        while True:
            n = sum(int(x) ** 2 for x in str(n))
            if n == 1:
                return True
            elif n in unhappy:
                return False
            else:
                unhappy.add(n)


n = 19
sol = Solution()
res = sol.isHappy(n)
print(res)
