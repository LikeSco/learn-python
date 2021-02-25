#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution:

    def twoSum(self, nums, target):
        result = []
        val = {}
        i = 0

        for item in nums:
            val[i] = item
            i += 1

        for a in val.keys():
            if len(result) == 0:
                for b in val.keys():
                    if len(result) == 0:
                        if a != b:
                            if target == val[a] + val[b]:
                                result.append(a)
                                result.append(b)
        return result


numsV = [2, 7, 11, 15]
targetV = 9
sol = Solution()
ts = sol.twoSum(numsV, targetV)
print(ts)
