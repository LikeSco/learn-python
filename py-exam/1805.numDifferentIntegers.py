#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

"""
给你一个字符串 word ，该字符串由数字和小写英文字母组成。

请你用空格替换每个不是数字的字符。例如，"a123bc34d8ef34" 将会变成 " 123  34 8  34" 。注意，剩下的这些整数为（相邻彼此至少有一个空格隔开）："123"、"34"、"8" 和 "34" 。

返回对 word 完成替换后形成的 不同 整数的数目。

只有当两个整数的 不含前导零 的十进制表示不同， 才认为这两个整数也不同。
"""


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        if len(word) == 0:
            return 0
        s = re.sub('[a-z]', ' ', word)
        nums = s.split(' ')
        while '' in nums:
            nums.remove('')
        if len(nums) == 1 or len(nums) == 0:
            return len(nums)
        for i in range(len(nums)):
            list_item = list(nums[i])
            while list_item[0] == '0' and len(list_item) >= 2:
                list_item.remove(list_item[0])
            nums[i] = ''.join(list_item)
        nums = set(nums)
        return len(nums)


word = "a123bc034d8ef34"
sol = Solution()
res = sol.numDifferentIntegers(word)
print(res)
