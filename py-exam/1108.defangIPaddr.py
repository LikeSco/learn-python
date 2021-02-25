#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给你一个有效的 IPv4 地址 address，返回这个 IP 地址的无效化版本。

所谓无效化 IP 地址，其实就是用 "[.]" 代替了每个 "."。
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        list_add = list(address)
        for i in range(len(list_add)):
            if list_add[i] == '.':
                list_add[i] = '[.]'
        return ''.join(list_add)


address = "1.1.1.1"
sol = Solution()
res = sol.defangIPaddr(address)
print(res)
