#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个整数数组 salary ，数组里每个数都是 唯一 的，其中 salary[i] 是第 i 个员工的工资。

请你返回去掉最低工资和最高工资以后，剩下员工工资的平均值。
"""


class Solution:
    def average(self, salary) -> float:
        salary.remove(max(salary))
        salary.remove(min(salary))
        total = sum(salary)
        return total / len(salary)


salary = [6000, 5000, 4000, 3000, 2000, 1000]
sol = Solution()
res = sol.average(salary)
print(res)
