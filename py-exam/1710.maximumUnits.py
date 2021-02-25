#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
请你将一些箱子装在 一辆卡车 上。给你一个二维数组 boxTypes ，其中 boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi] ：

numberOfBoxesi 是类型 i 的箱子的数量。
numberOfUnitsPerBoxi 是类型 i 每个箱子可以装载的单元数量。
整数 truckSize 表示卡车上可以装载 箱子 的 最大数量 。只要箱子数量不超过 truckSize ，你就可以选择任意箱子装到卡车上。

返回卡车可以装载 单元 的 最大 总数。
"""


class Solution:
    def maximumUnits(self, boxTypes, truckSize: int) -> int:
        boxNums = []
        boxUnits = []
        total_size = 0
        total_amount = 0
        for item in boxTypes:
            boxNums.append(item[0])
            boxUnits.append(item[1])
        i = 0
        while i < len(boxUnits):
            max_unit = max(boxUnits)
            index = boxUnits.index(max_unit)
            if boxUnits[index] == max_unit:
                if total_size + boxNums[index] <= truckSize:
                    total_size += boxNums[index]
                    total_amount += boxNums[index] * boxUnits[index]
                    boxUnits[index] = 0
                    boxNums[index] = 0
                else:
                    last_size = truckSize - total_size
                    total_amount += last_size * boxUnits[index]
                    break
            i += 1

        return total_amount


boxTypes = [[5, 10], [2, 5], [4, 7], [3, 9]]
truckSize = 10
sol = Solution()
res = sol.maximumUnits(boxTypes, truckSize)
print(res)
