#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        romanRegulation = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        s1 = s
        result = 0
        if 'IV' in s1:
            result += 4
            s1 = s1.replace('IV', '')
        if 'IX' in s1:
            result += 9
            s1 = s1.replace('IX', '')
        if 'XL' in s1:
            result += 40
            s1 = s1.replace('XL', '')
        if 'XC' in s1:
            result += 90
            s1 = s1.replace('XC', '')
        if 'CD' in s1:
            result += 400
            s1 = s1.replace('CD', '')
        if 'CM' in s1:
            result += 900
            s1 = s1.replace('CM', '')

        for ch in s1:
            if ch in romanRegulation:
                result += romanRegulation[ch]

        return result


s = 'MCMXCIV'
sol = Solution()
res = sol.romanToInt(s)
print(res)
