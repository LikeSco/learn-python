#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
你在和朋友一起玩 猜数字（Bulls and Cows）游戏，该游戏规则如下：

你写出一个秘密数字，并请朋友猜这个数字是多少。
朋友每猜测一次，你就会给他一个提示，告诉他的猜测数字中有多少位属于数字和确切位置都猜对了（称为“Bulls”, 公牛），有多少位属于数字猜对了但是位置不对（称为“Cows”, 奶牛）。
朋友根据提示继续猜，直到猜出秘密数字。
请写出一个根据秘密数字和朋友的猜测数返回提示的函数，返回字符串的格式为 xAyB ，x 和 y 都是数字，A 表示公牛，用 B 表示奶牛。

xA 表示有 x 位数字出现在秘密数字中，且位置都与秘密数字一致。
yB 表示有 y 位数字出现在秘密数字中，但位置与秘密数字不一致。
请注意秘密数字和朋友的猜测数都可能含有重复数字，每位数字只能统计一次。
"""


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        list_secret = list(secret)
        list_guess = list(guess)
        count_A = 0
        count_B = 0
        list_num = []
        list_remain = []
        for i in range(len(list_secret)):
            if list_secret[i] == list_guess[i]:
                count_A += 1
            else:
                list_remain.append(list_secret[i])
                list_num.append(list_guess[i])

        for item in list_remain:
            if item in list_num:
                count_B += 1
                list_num.remove(item)

        return str(count_A) + 'A' + str(count_B) + 'B'


secret = "1123"
guess = "0111"
sol = Solution()
res = sol.getHint(secret, guess)
print(res)
