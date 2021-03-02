#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个整数 n，返回 n! 结果尾数中零的数量。
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 1
        for i in range(1, n + 1):
            result = result * i
        # print(result)
        count = 0
        list_result = list(str(result))
        list_result.reverse()
        for num in list_result:
            if num == '0':
                count += 1
            else:
                break

        return count


n = 7
sol = Solution()
res = sol.trailingZeroes(n)
print(res)
