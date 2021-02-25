#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2
"""
import math


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        # if dividend == 0 or divisor == 0:
        #     return 0
        # if divisor == 1:
        #     if -math.pow(2, 31) <= dividend <= math.pow(2, 31) - 1:
        #         return dividend
        #     else:
        #         return int(math.pow(2, 31) - 1)
        # if divisor == -1:
        #     if -math.pow(2, 31) <= -dividend <= math.pow(2, 31) - 1:
        #         return -dividend
        #     else:
        #         return int(math.pow(2, 31) - 1)
        dividend1 = int(str(dividend).replace('-', ''))
        divisor1 = int(str(divisor).replace('-', ''))
        # sum1 = divisor1
        # i = 1
        # j = 0
        # sum2 = divisor1
        # while sum1 <= dividend1:
        #     sum1 += sum1
        #     i += i
        # while sum2 < sum1 - dividend1:
        #     sum2 += divisor1
        #     j += 1
        # i = i - j
        i = dividend1 // divisor1
        if ('-' in str(dividend) and '-' in str(divisor)) or ('-' not in str(dividend) and '-' not in str(divisor)):
            pass
        else:
            i = -i
        if -math.pow(2, 31) > i or i > math.pow(2, 31) - 1:
            return int(math.pow(2, 31) - 1)
        else:
            return i


dividend = -2147483648
divisor = 2
sol = Solution()
res = sol.divide(dividend, divisor)
print(res)
