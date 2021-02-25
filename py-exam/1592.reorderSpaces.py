#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个字符串 text ，该字符串由若干被空格包围的单词组成。每个单词由一个或者多个小写英文字母组成，并且两个单词之间至少存在一个空格。题目测试用例保证 text 至少包含一个单词 。

请你重新排列空格，使每对相邻单词之间的空格数目都 相等 ，并尽可能 最大化 该数目。如果不能重新平均分配所有空格，请 将多余的空格放置在字符串末尾 ，这也意味着返回的字符串应当与原 text 字符串的长度相等。

返回 重新排列空格后的字符串 。
"""


class Solution:
    def reorderSpaces(self, text: str) -> str:
        if ' ' not in text:
            return text
        space_count = text.count(' ')
        arr = text.split(' ')
        list_word = []
        for item in arr:
            if item != '':
                list_word.append(item)
        if len(list_word) == 1:
            space = ''
            for a in range(space_count):
                space += ' '
            return list_word[0] + space

        div = space_count // (len(list_word) - 1)
        mod = space_count % (len(list_word) - 1)
        avg_space = ''
        mod_space = ''
        for i in range(div):
            avg_space += ' '
        for j in range(mod):
            mod_space += ' '
        result = ''
        for word in list_word[0:-1]:
            result += word
            result += avg_space
        result = result + list_word[-1] + mod_space

        return result


text = " practice   makes   perfect"
sol = Solution()
res = sol.reorderSpaces(text)
print(res)
