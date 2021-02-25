#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math

"""首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：

如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。
注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0 。

本题中的空白字符只包括空格字符 ' ' 。
假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        a = ''
        digits = '0123456789'
        l = []

        s1 = s.strip()
        if len(s1) == 0:
            return 0

        else:
            if s1[0] == '-' or s1[0] == '+':
                a = s1[0]
                s1 = s1[1:]

            for item in s1:
                if item in digits:
                    l.append(item)
                else:
                    break

            if len(l) == 0:
                return 0
            else:
                result = a + ''.join(l)
                atoiResult = int(result)
                if atoiResult > math.pow(2, 31) - 1:
                    return int(math.pow(2, 31) - 1)
                elif atoiResult < -math.pow(2, 31):
                    return int(-math.pow(2, 31))
                else:
                    return atoiResult


s = "   -898 888k"    # 输出 -898
sol = Solution()
res = sol.myAtoi(s)
print(res)
