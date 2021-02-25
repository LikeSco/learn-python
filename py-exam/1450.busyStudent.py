#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你两个整数数组 startTime（开始时间）和 endTime（结束时间），并指定一个整数 queryTime 作为查询时间。

已知，第 i 名学生在 startTime[i] 时开始写作业并于 endTime[i] 时完成作业。

请返回在查询时间 queryTime 时正在做作业的学生人数。形式上，返回能够使 queryTime 处于区间 [startTime[i], endTime[i]]（含）的学生人数。
"""


class Solution:
    def busyStudent(self, startTime, endTime, queryTime: int) -> int:
        count = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                count += 1
        return count


startTime = [9, 8, 7, 6, 5, 4, 3, 2, 1]
endTime = [10, 10, 10, 10, 10, 10, 10, 10, 10]
queryTime = 5
sol = Solution()
res = sol.busyStudent(startTime, endTime, queryTime)
print(res)
