#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个由大小写英文字母组成的字符串 s 。

一个整理好的字符串中，两个相邻字符 s[i] 和 s[i+1]，其中 0<= i <= s.length-2 ，要满足如下条件:

若 s[i] 是小写字符，则 s[i+1] 不可以是相同的大写字符。
若 s[i] 是大写字符，则 s[i+1] 不可以是相同的小写字符。
请你将字符串整理好，每次你都可以从字符串中选出满足上述条件的 两个相邻 字符并删除，直到字符串整理好为止。

请返回整理好的 字符串 。题目保证在给出的约束条件下，测试样例对应的答案是唯一的。

注意：空字符串也属于整理好的字符串，尽管其中没有任何字符。
"""


class Solution:
    def makeGood(self, s: str) -> str:
        ascii_lower = 'abcdefghijklmnopqrstuvwxyz'
        ascii_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        dict_ch = {}
        for i in range(len(ascii_lower)):
            dict_ch[ascii_lower[i]] = ascii_upper[i]

        if len(s) <= 1:
            return s

        j = 0
        while (j != len(s) - 1) and len(s) != 0:

            list_s = list(s)
            for j in range(len(s)):
                if j < len(s) - 1:
                    if list_s[j] in dict_ch.keys():
                        if dict_ch[list_s[j]] == list_s[j + 1]:
                            list_s[j] = ''
                            list_s[j + 1] = ''
                            s = ''.join(list_s)
                            j = 0
                            break
                    if list_s[j + 1] in dict_ch.keys():
                        if list_s[j] == dict_ch[list_s[j + 1]]:
                            list_s[j] = ''
                            list_s[j + 1] = ''
                            s = ''.join(list_s)
                            j = 0
                            break
        return s


s = "leEeetcode"
sol = Solution()
res = sol.makeGood(s)
print(res)
