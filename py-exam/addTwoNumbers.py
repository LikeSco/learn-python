#!/usr/bin/python
# -*- coding: UTF-8 -*-

l1 = [2, 4, 3]
l2 = [5, 6, 4]
l3 = []

l1.reverse()
l2.reverse()

x = ''.join(str(i) for i in l1)
y = ''.join(str(i) for i in l2)

z = int(x) + int(y)

for item in str(z):
    l3.append(int(item))

l3.reverse()
print(l3)
