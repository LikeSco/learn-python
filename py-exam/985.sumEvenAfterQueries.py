#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给出一个整数数组 A 和一个查询数组 queries。

对于第 i 次查询，有 val = queries[i][0], index = queries[i][1]，我们会把 val 加到 A[index] 上。然后，第 i 次查询的答案是 A 中偶数值的和。

（此处给定的 index = queries[i][1] 是从 0 开始的索引，每次查询都会永久修改数组 A。）

返回所有查询的答案。你的答案应当以数组 answer 给出，answer[i] 为第 i 次查询的答案。
"""


class Solution:
    def sumEvenAfterQueries(self, A, queries):
        result = []
        sum_evens = sum([a for a in A if a % 2 == 0])
        for item in queries:
            index = item[1]
            new_a = A[index] + item[0]
            if A[index] % 2 == 0 and new_a % 2 == 0:
                sum_evens = sum_evens - A[index] + new_a
            elif A[index] % 2 != 0 and new_a % 2 == 0:
                sum_evens = sum_evens + new_a
            elif A[index] % 2 == 0 and new_a % 2 != 0:
                sum_evens = sum_evens - A[index]

            A[index] = new_a
            result.append(sum_evens)
        return result


A = [1, 2, 3, 4]
queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
sol = Solution()
res = sol.sumEvenAfterQueries(A, queries)
print(res)
