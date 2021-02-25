#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个混合了数字和字母的字符串 s，其中的字母均为小写英文字母。

请你将该字符串重新格式化，使得任意两个相邻字符的类型都不同。也就是说，字母后面应该跟着数字，而数字后面应该跟着字母。

请你返回 重新格式化后 的字符串；如果无法按要求重新格式化，则返回一个 空字符串 。
"""


class Solution:
    def reformat(self, s: str) -> str:
        # charactors = 'abcdefghijklmnopqrstuvwxyz'
        digits = '0123456789'
        list_nums = []
        list_ch = []
        for item in s:
            if item in digits:
                list_nums.append(item)
            else:
                list_ch.append(item)
        if abs(len(list_ch) - len(list_nums)) >= 2:
            return ''
        result = ''
        if len(list_ch) == len(list_nums):
            for i in range(len(list_nums)):
                result += list_ch[i]
                result += list_nums[i]
        elif len(list_ch) > len(list_nums):
            for i in range(len(list_nums)):
                result += list_ch[i]
                result += list_nums[i]
            result += list_ch[-1]
        else:
            for i in range(len(list_ch)):
                result += list_nums[i]
                result += list_ch[i]
            result += list_nums[-1]
        return result


s = "a0b1c2"
sol = Solution()
res = sol.reformat(s)
print(res)
