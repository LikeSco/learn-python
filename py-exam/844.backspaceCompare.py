#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。

注意：如果对空文本输入退格字符，文本继续为空。
"""


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        list_val = [S, T]
        for j in range(len(list_val)):
            while '#' in list_val[j]:
                list_S = list(list_val[j])
                for i in range(len(list_S)):
                    if list_S[i] == '#':
                        if i == 0:
                            list_S[i] = ''
                        else:
                            list_S[i] = ''
                            list_S[i - 1] = ''
                        list_val[j] = ''.join(list_S)
                        break
        if list_val[0] == list_val[1]:
            return True
        return False


S = "ab##"
T = "c#d#"
sol = Solution()
res = sol.backspaceCompare(S, T)
print(res)
