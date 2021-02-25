#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
编写一个程序判断给定的数是否为丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。
"""


class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False
        if num == 1:
            return True
        ugly_nums = [2, 3, 5]
        result = 0
        while True:
            if num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
                return False
            for item in ugly_nums:
                if num % item == 0:
                    result = int(num / item)
                    num = result
                if result == 1:
                    return True


n = 1024
sol = Solution()
res = sol.isUgly(n)
print(res)
