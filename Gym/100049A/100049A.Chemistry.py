#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/1/28 13:13
# @File     : 100049A.Chemistry.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆

index = 0
string = input()
vowels = ['a', 'e', 'i', 'o', 'u']

while index < len(string):
    if string[index] in vowels:
        string = string[:index] + string[index+2:]
    index += 1

print(string)
