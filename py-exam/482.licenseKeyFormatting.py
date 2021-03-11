#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
有一个密钥字符串 S ，只包含字母，数字以及 '-'（破折号）。其中， N 个 '-' 将字符串分成了 N+1 组。

给你一个数字 K，请你重新格式化字符串，使每个分组恰好包含 K 个字符。特别地，第一个分组包含的字符个数必须小于等于 K，但至少要包含 1 个字符。两个分组之间需要用 '-'（破折号）隔开，并且将所有的小写字母转换为大写字母。

给定非空字符串 S 和数字 K，按照上面描述的规则进行格式化。
"""
import re


class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        head = ''
        arr = S.split('-')
        S1 = ''.join(arr).upper()
        a = len(S1) % K
        if a != 0:
            head = S1[0:a]
            S1 = S1[a:]

        result = re.findall(r'.{' + str(K) + '}', S1)
        if head != '':
            result.insert(0, head)
        return '-'.join(result)


S = "2-5g-3-J"
K = 2
sol = Solution()
res = sol.licenseKeyFormatting(S, K)
print(res)
