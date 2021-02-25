# !/usr/bin/python3

import random
import string
import json


totalGuessPool = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


def randomValue(len):
    """
    :param len: 随机码长度
    :return: 随机码数字字母组合
    """
    strV = []
    for i in range(len):
        strV.append(random.choice(totalGuessPool))
    return ''.join(strV)


def generateCode(codeLen, codeCount):
    """
    :param codeLen: 随机码长度
    :param codeCount: 随机码个数
    :return:
    """

    # {} 是一个空字典 dict !
    # nlist = {}
    i = 0
    dumpSet = set()

    while i < codeCount:
        val = randomValue(codeLen)
        while val in dumpSet:
            val = randomValue(codeLen)
        dumpSet.add(val)
        i += 1

    # print(dumpSet)
    return dumpSet

    # print(json.dumps(nlist))


output = generateCode(6, 100)

with open('output.json', 'w') as writefs:
    writefs.write(json.dumps(list(output)))
    writefs.close()
