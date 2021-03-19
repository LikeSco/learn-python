#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个字符串 time ，格式为 hh:mm（小时：分钟），其中某几位数字被隐藏（用 ? 表示）。
有效的时间为 00:00 到 23:59 之间的所有时间，包括 00:00 和 23:59 。
替换 time 中隐藏的数字，返回你可以得到的最晚有效时间。
"""


class Solution:
    def maximumTime(self, time: str) -> str:
        list_time = list(time)
        if list_time[0] == '?':
            if list_time[1] == '?':
                list_time[0] = '2'
                list_time[1] = '3'
            elif int(list_time[1]) <= 3:
                list_time[0] = '2'
            else:
                list_time[0] = '1'
        if list_time[1] == '?':
            if list_time[0] == '2':
                list_time[1] = '3'
            else:
                list_time[1] = '9'
        if list_time[3] == '?':
            list_time[3] = '5'
        if list_time[4] == '?':
            list_time[4] = '9'

        return ''.join(list_time)


time = "0?:3?"
sol = Solution()
res = sol.maximumTime(time)
print(res)
