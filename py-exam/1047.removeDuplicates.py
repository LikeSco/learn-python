#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。

在 S 上反复执行重复项删除操作，直到无法继续删除。

在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。
"""


class Solution:
    def removeDuplicates(self, S: str) -> str:
        list_S = ['']
        for ch in S:
            if ch == list_S[-1]:
                list_S.pop()
            else:
                list_S.append(ch)
        S = ''.join(list_S)
        return S


S = "abbaca"
sol = Solution()
res = sol.removeDuplicates(S)
print(res)
