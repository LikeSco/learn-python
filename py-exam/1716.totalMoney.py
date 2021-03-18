#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Hercy 想要为购买第一辆车存钱。他 每天 都往力扣银行里存钱。

最开始，他在周一的时候存入 1 块钱。从周二到周日，他每天都比前一天多存入 1 块钱。在接下来每一个周一，他都会比 前一个周一 多存入 1 块钱。

给你 n ，请你返回在第 n 天结束的时候他在力扣银行总共存了多少块钱。
"""


class Solution:
    def totalMoney(self, n: int) -> int:
        week_days = 7
        m = 1
        money = 0
        while n >= 7:
            i = m
            d = 1
            while d <= week_days:
                money += i
                i += 1
                d += 1
            m += 1
            n -= week_days

        i = m
        d = 1
        while d <= n:
            money += i
            i += 1
            d += 1
        return money


n = 20
sol = Solution()
res = sol.totalMoney(n)
print(res)
