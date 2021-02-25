#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。

你可以按任意顺序返回答案。
"""


class Solution:
    def commonChars(self, A):
        A1 = []
        for ch in A[0]:
            flag = True
            for i in range(1, len(A)):
                if ch not in A[i]:
                    flag = False
                    break
                else:
                    word = list(A[i])
                    word.remove(ch)
                    A[i] = ''.join(word)
            if flag:
                A1.append(ch)

        return A1


A = ["cool", "lock", "cook"]
sol = Solution()
res = sol.commonChars(A)
print(res)
