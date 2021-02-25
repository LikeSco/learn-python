#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        # if len(s.strip()) == 0:
        #     return ''
        arr = s.split(' ')
        word_list = []
        for item in arr:
            if len(item) > 0:
                list_item = list(item)
                list_item.reverse()
                word_list.append(''.join(list_item))
        return ' '.join(word_list)


s = "Let's take LeetCode contest"
sol = Solution()
res = sol.reverseWords(s)
print(res)
