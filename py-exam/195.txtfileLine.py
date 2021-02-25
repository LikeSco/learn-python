#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个文本文件 file.txt，请只打印这个文件中的第十行。
"""

with open('file.txt', 'r', encoding='utf-8') as txt_file:
    lines = txt_file.readlines()
    txt_file.close()

if len(lines) >= 10:
    print(lines[9].strip())
