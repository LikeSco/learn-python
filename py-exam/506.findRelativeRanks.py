#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold Medal", "Silver Medal", "Bronze Medal"）。

(注：分数越高的选手，排名越靠前。)
"""


class Solution:
    def findRelativeRanks(self, nums):
        dict_rank = {}
        for i, n in enumerate(nums):
            dict_rank[n] = str(i+1)
        nums.sort(reverse=True)
        dict_rank1 = {}
        for j in range(len(nums)):
            if j == 0:
                dict_rank1[nums[j]] = "Gold Medal"
            elif j == 1:
                dict_rank1[nums[j]] = "Silver Medal"
            elif j == 2:
                dict_rank1[nums[j]] = "Bronze Medal"
            else:
                dict_rank1[nums[j]] = str(j+1)
        for rank in dict_rank:
            for rank1 in dict_rank1:
                if rank1 == rank:
                    dict_rank[rank] = dict_rank1[rank1]
                    break
        return list(dict_rank.values())


nums = [10,3,8,9,4]
sol = Solution()
res = sol.findRelativeRanks(nums)
print(res)
