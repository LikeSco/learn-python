#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个字符串 s ，请你根据下面的算法重新构造字符串：

从 s 中选出 最小 的字符，将它 接在 结果字符串的后面。
从 s 剩余字符中选出 最小 的字符，且该字符比上一个添加的字符大，将它 接在 结果字符串后面。
重复步骤 2 ，直到你没法从 s 中选择字符。
从 s 中选出 最大 的字符，将它 接在 结果字符串的后面。
从 s 剩余字符中选出 最大 的字符，且该字符比上一个添加的字符小，将它 接在 结果字符串后面。
重复步骤 5 ，直到你没法从 s 中选择字符。
重复步骤 1 到 6 ，直到 s 中所有字符都已经被选过。
在任何一步中，如果最小或者最大字符不止一个 ，你可以选择其中任意一个，并将其添加到结果字符串。

请你返回将 s 中字符重新排序后的 结果字符串 。
"""


class Solution:
    def sortString(self, s: str) -> str:
        arr = list(s)
        result = ''
        while len(arr) != 0:
            list_s = list(set(arr))
            i = 0
            while len(list_s) != 0:
                min_ch = min(list_s)
                result += min_ch
                list_s.remove(min_ch)
                arr.remove(min_ch)
                i += 1

            list_s = list(set(arr))
            j = 0
            while len(list_s) != 0:
                max_ch = max(list_s)
                result += max_ch
                list_s.remove(max_ch)
                arr.remove(max_ch)
                j += 1

        return result


s = "aabfufg"
sol = Solution()
res = sol.sortString(s)
print(res)
