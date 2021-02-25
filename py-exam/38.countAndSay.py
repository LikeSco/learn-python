#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个正整数 n ，输出外观数列的第 n 项。

「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。

你可以将其视作是由递归公式定义的数字字符串序列：

countAndSay(1) = "1"
countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        # regulation = {
        #     1: '1',
        #     2: '11',
        #     3: '21',
        #     4: '1211',
        #     5: '111221',
        # }
        i = 1
        result = '1'
        while i < n:
            i += 1
            # print(i)
            l1 = []
            l2 = []
            for a in range(len(result)):
                if a < len(result) - 1:
                    if result[a] == result[a + 1]:
                        l1.append(result[a])
                    else:
                        l1.append(result[a])
                        l2.append(l1)
                        l1 = []
                else:
                    l1.append(result[a])
                    l2.append(l1)
                    l1 = []
            # print(l2)
            res1 = ''
            for item in l2:
                res1 += str(item.count(item[0])) + item[0]
            result = res1
            # print(result)
        return result


n = 9
sol = Solution()
res = sol.countAndSay(n)
print(res)
