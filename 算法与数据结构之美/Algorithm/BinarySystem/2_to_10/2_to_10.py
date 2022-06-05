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
num_2 = input()     # 输入的二进制数字符串
# print(int(num_2, B))
num_10 = 0

for i in range(len(num_2)):     # 明确循环次数的时候用for循环
    num_10 += int(num_2[::-1][i]) * (2 ** i)

print(num_10)
