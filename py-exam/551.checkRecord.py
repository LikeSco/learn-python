#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个字符串来代表一个学生的出勤记录，这个记录仅包含以下三个字符：

'A' : Absent，缺勤
'L' : Late，迟到
'P' : Present，到场
如果一个学生的出勤记录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。

你需要根据这个学生的出勤记录判断他是否会被奖赏。
"""


class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A') <= 1 and 'LLL' not in s:
            return True
        return False


s = "PPALLP"
sol = Solution()
res = sol.checkRecord(s)
print(res)
