#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个仅包含小写英文字母和 '?' 字符的字符串 s，请你将所有的 '?' 转换为若干小写字母，使最终的字符串不包含任何 连续重复 的字符。

注意：你 不能 修改非 '?' 字符。

题目测试用例保证 除 '?' 字符 之外，不存在连续重复的字符。

在完成所有转换（可能无需转换）后返回最终的字符串。如果有多个解决方案，请返回其中任何一个。可以证明，在给定的约束条件下，答案总是存在的。
"""


class Solution:
    def modifyString(self, s: str) -> str:
        if '?' not in s:
            return s
        if s == '?':
            return 'a'
        ascii_lower = 'abcdefghijklmnopqrstuvwxyz'
        list_s = list(s)
        for i in range(len(list_s)):
            if list_s[i] == '?':
                if i == 0:
                    for ch in ascii_lower:
                        if ch != list_s[i + 1]:
                            list_s[i] = ch
                            break
                elif i == len(list_s) - 1:
                    for ch in ascii_lower:
                        if ch != list_s[i - 1]:
                            list_s[i] = ch
                            break
                else:
                    for ch in ascii_lower:
                        if ch != list_s[i - 1] and ch != list_s[i + 1]:
                            list_s[i] = ch
                            break
        return ''.join(list_s)


s = "??yw?ipkj?"
sol = Solution()
res = sol.modifyString(s)
print(res)
