#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定两个字符串, A 和 B。

A 的旋转操作就是将 A 最左边的字符移动到最右边。 例如, 若 A = 'abcde'，在移动一次之后结果就是'bcdea' 。如果在若干次旋转操作之后，A 能变成B，那么返回True。
"""


class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A.strip() == B.strip() == '':
            return True
        list_A = list(A)
        list_B = list(B)
        count = 0
        while count < len(A) - 1:
            for ch in list_A:
                list_A.remove(ch)
                list_A.append(ch)
                break
            if list_A == list_B:
                return True
            count += 1
        return False


A = 'abcde'
B = 'cdeab'
sol = Solution()
res = sol.rotateString(A, B)
print(res)
