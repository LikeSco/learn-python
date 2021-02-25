#!/usr/bin/python3

import re
from os import path
import sys

readFile = "phoneNumber.txt"
writeFile = "result.txt"

currentDir = path.dirname(__file__)
resourcePath = path.join(currentDir, readFile)
outputPath = path.join(currentDir, writeFile)

pattern = re.compile(r'^(\d{3}-|\(\d{3}\)\s)\d{3}-\d{4}$')
result = []

with open(resourcePath, "r") as readfs:
    txtLines = readfs.readlines()
    for line in txtLines:
        trimedLine = line.strip(' \n')
        pNum = re.match(pattern, trimedLine)
        if pNum:
            print(trimedLine)
            result.append(trimedLine)
    readfs.close()

with open(outputPath, "w") as writefs:
    writefs.write('\n'.join(result))
    writefs.close()
