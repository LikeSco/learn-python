#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
在柠檬水摊上，每一杯柠檬水的售价为 5 美元。

顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。

每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。

注意，一开始你手头没有任何零钱。

如果你能给每位顾客正确找零，返回 true ，否则返回 false 。
"""


class Solution:
    def lemonadeChange(self, bills) -> bool:
        moneys_five = []
        money_ten = []
        for bill in bills:
            if bill == 5:
                moneys_five.append(bill)
            elif bill == 10:
                if len(moneys_five) == 0:
                    return False
                moneys_five.pop()
                money_ten.append(bill)
            else:
                if len(moneys_five) != 0 and len(money_ten) != 0:
                    moneys_five.pop()
                    money_ten.pop()
                elif len(moneys_five) >= 3:
                    moneys_five.pop()
                    moneys_five.pop()
                    moneys_five.pop()
                else:
                    return False

        return True


bills = [5, 5, 5, 10, 20]
sol = Solution()
res = sol.lemonadeChange(bills)
print(res)
