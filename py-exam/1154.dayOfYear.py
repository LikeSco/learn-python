#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个按 YYYY-MM-DD 格式表示日期的字符串 date，请你计算并返回该日期是当年的第几天。

通常情况下，我们认为 1 月 1 日是每年的第 1 天，1 月 2 日是每年的第 2 天，依此类推。每个月的天数与现行公元纪年法（格里高利历）一致。
"""


class Solution:
    def dayOfYear(self, date: str) -> int:
        arr = date.split('-')
        year = int(arr[0])
        month = int(arr[1])
        day = int(arr[2])
        dic = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
            dic[1] = 29
        return sum(dic[:month - 1]) + day


date = "2003-03-01"
sol = Solution()
res = sol.dayOfYear(date)
print(res)