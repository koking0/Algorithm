#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/B/11 11:26
# @File     : 2_to_10.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
base = int(input("请输入任意进制："))
num_any = input("请输入的任意进制数字符串：")
num_10 = 0

num_any = list(num_any.upper())
for i in range(len(num_any)):
    if num_any[i].isalpha():     # 如果当前元素为字母
        num_any[i] = ord(num_any[i]) - ord("A") + 10  # 转换为相应的数字

for i in range(len(num_any)):     # 明确循环次数的时候用for循环
    num_10 += int(num_any[::-1][i]) * (base ** i)

print(num_10)
