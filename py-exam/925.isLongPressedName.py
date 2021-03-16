#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。

你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。
"""


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        list_name = list(name)
        list_typed = list(typed)
        if list(set(list_typed)) != list(set(list_name)) or len(list_name) > len(list_typed):
            return False
        if list_name[0] != list_typed[0] or list_name[-1] != list_typed[-1]:
            return False
        i = 0
        j = 0
        count = 0
        while 0 <= i < len(name):
            if list_name[i] == list_typed[j]:
                i += 1
                j += 1
                count = 0
            elif count == 0:
                i -= 1
                count += 1
            else:
                return False
        if i < 0:
            return False
        if set(list_typed[j - 1:]) == set(list_name[i - 1:]):
            return True
        else:
            return False


name = "saeed"
typed = "ssaaedd"
sol = Solution()
res = sol.isLongPressedName(name, typed)
print(res)
