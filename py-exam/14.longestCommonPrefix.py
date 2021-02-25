#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。


class Solution:
    def longestCommonPrefix(self, strs):
        l1 = []
        l2 = []
        i = 0
        flag = True

        if len(strs) == 0:
            return ""
        else:
            while i <= min(len(a) for a in strs) - 1:

                if flag:
                    for item in strs:
                        if len(l1) == 0:
                            l1.append(item[i])

                        else:
                            if item[i] not in l1:
                                flag = False
                    if flag:
                        l2.append(l1[0])
                        l1 = []
                i += 1

            return ''.join(l2).strip()


strVal = ["flower", "flow", "flight"]   # 输出: "fl"
sol = Solution()
longestVal = sol.longestCommonPrefix(strVal)
print(longestVal)
