#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
假设Andy和Doris想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。

你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设总是存在一个答案。
"""


class Solution:
    def findRestaurant(self, list1, list2):
        index = len(list1) + len(list2)
        result = []

        for i in range(len(list1)):
            if list1[i] in list2:
                index1 = i + list2.index(list1[i])
                if index1 < index:
                    index = index1
                    result = [list1[i]]
                elif index1 == index:
                    result.append(list1[i])
        return result


list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Shogun", "Burger King"]
sol = Solution()
res = sol.findRestaurant(list1, list2)
print(res)
