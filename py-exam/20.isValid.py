#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        else:
            pairs = {")": "(", "]": "[", "}": "{"}
            p_list = list()

            for ch in s:
                if ch in pairs.keys():
                    if len(p_list) == 0 or p_list[-1] != pairs[ch]:
                        return False
                    else:
                        p_list.pop()
                else:
                    p_list.append(ch)

            return not p_list


s = "(([]){})"
sol = Solution()
res = sol.isValid(s)
print(res)
