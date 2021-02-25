#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math


class Solution:
    def reverse(self, x: int):

        y = []
        n = ''
        z = str(x)

        if '-' in z:
            n = '-'
            z = z.replace("-", "")

        for a in z:
            y.append(a)

        y.reverse()
        result = n + ''.join(y)

        reverseResult = int(result)

        if (reverseResult >= math.pow(2, 31) - 1 or reverseResult <= -math.pow(2, 31)):
            return 0
        else:
            return reverseResult


val = -112346498
sol = Solution()
rev = sol.reverse(val)
print(rev)
