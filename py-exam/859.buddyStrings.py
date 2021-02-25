#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，就返回 true ；否则返回 false 。

交换字母的定义是取两个下标 i 和 j （下标从 0 开始），只要 i!=j 就交换 A[i] 和 A[j] 处的字符。例如，在 "abcd" 中交换下标 0 和下标 2 的元素可以生成 "cbad" 。
"""


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if A.strip() == '' or B.strip() == '' or len(A.strip()) == 1:
            return False
        if A == B and A.count(A[0]) == len(A):
            return True
        if A == B:
            for item in A:
                if A.count(item) >= 2:
                    return True

        if len(A) == len(B):
            dict_ch = {}
            for i in range(len(A)):
                if A[i] != B[i]:
                    dict_ch[i] = A[i]

            list_B = []
            if len(dict_ch) == 2:
                for key in dict_ch:
                    list_B.append(B[key])
                list_B.reverse()
                if list(dict_ch.values()) == list_B:
                    return True
        return False


A = "aaaaaaabc"
B = "aaaaaaacb"
sol = Solution()
res = sol.buddyStrings(A, B)
print(res)
