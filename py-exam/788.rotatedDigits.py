#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
我们称一个数 X 为好数, 如果它的每位数字逐个地被旋转 180 度后，我们仍可以得到一个有效的，且和 X 不同的数。要求每位数字都要被旋转。

如果一个数的每位数字被旋转以后仍然还是一个数字， 则这个数是有效的。0, 1, 和 8 被旋转后仍然是它们自己；2 和 5 可以互相旋转成对方（在这种情况下，它们以不同的方向旋转，换句话说，2 和 5 互为镜像）；6 和 9 同理，除了这些以外其他的数字旋转以后都不再是有效的数字。

现在我们有一个正整数 N, 计算从 1 到 N 中有多少个数 X 是好数？
"""


class Solution:
    def rotatedDigits(self, N: int) -> int:
        good_nums = [2, 5, 6, 9]
        valid_nums = [0, 1, 8]
        count = 0
        nums = list(range(1, N + 1))
        for num in nums:
            if num in good_nums:
                count += 1
            if len(str(num)) >= 2:
                val = list(str(num))
                result = set()
                for n in val:
                    n1 = int(n)
                    if n1 in good_nums:
                        result.add('good')
                    elif n1 in valid_nums:
                        result.add('valid')
                    else:
                        result.add('invalid')
                        break
                result = list(result)
                result.sort()
                if result == ['good'] or result == ['good', 'valid']:
                    count += 1
        return count


N = 88
sol = Solution()
res = sol.rotatedDigits(N)
print(res)
