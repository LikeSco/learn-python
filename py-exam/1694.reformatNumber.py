#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个字符串形式的电话号码 number 。number 由数字、空格 ' '、和破折号 '-' 组成。

请你按下述方式重新格式化电话号码。

首先，删除 所有的空格和破折号。
其次，将数组从左到右 每 3 个一组 分块，直到 剩下 4 个或更少数字。剩下的数字将按下述规定再分块：
2 个数字：单个含 2 个数字的块。
3 个数字：单个含 3 个数字的块。
4 个数字：两个分别含 2 个数字的块。
最后用破折号将这些块连接起来。注意，重新格式化过程中 不应该 生成仅含 1 个数字的块，并且 最多 生成两个含 2 个数字的块。

返回格式化后的电话号码。
"""
import re


class Solution:
    def reformatNumber(self, number: str) -> str:
        number = re.sub('[^0-9]', '', number)
        nums = list(number)
        filter_nums = []
        last_number = []
        s = ''
        if len(number) % 3 == 1:
            last_number.append(''.join(nums[-4:-2]))
            last_number.append(''.join(nums[-2:]))
            nums = nums[0:-4]
        if len(number) % 3 == 2:
            last_number.append(''.join(nums[-2:]))
            nums = nums[0:-2]

        for i in range(len(nums)):
            s += nums[i]
            if i != 0 and (i+1) % 3 == 0:
                filter_nums.append(s)
                s = ''

        filter_nums = filter_nums + last_number
        return '-'.join(filter_nums)


number = "123 4-567"
sol = Solution()
res = sol.reformatNumber(number)
print(res)
