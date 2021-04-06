#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个数组 items ，其中 items[i] = [typei, colori, namei] ，描述第 i 件物品的类型、颜色以及名称。

另给你一条由两个字符串 ruleKey 和 ruleValue 表示的检索规则。

如果第 i 件物品能满足下述条件之一，则认为该物品与给定的检索规则 匹配 ：

ruleKey == "type" 且 ruleValue == typei 。
ruleKey == "color" 且 ruleValue == colori 。
ruleKey == "name" 且 ruleValue == namei 。
统计并返回 匹配检索规则的物品数量 。
"""


class Solution:
    def countMatches(self, items, ruleKey: str, ruleValue: str) -> int:
        dict_rule = {'type': 0, 'color': 1, 'name': 2}
        count = 0
        for item in items:
            if item[dict_rule[ruleKey]] == ruleValue:
                count += 1
        return count


items = [["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]]
ruleKey = "type"
ruleValue = "phone"
sol = Solution()
res = sol.countMatches(items, ruleKey, ruleValue)
print(res)
