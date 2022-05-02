#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/B/11 11:02
# @File     : 10_to_2.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
num_10 = int(input())  # 输入的十进制数
# print(bin(num_10).strip("0b"))
num_2 = []      # 其他语言可以用数组

while num_10:     # 不明确循环次数的时候用while循环
    num_2.append(num_10 % 2)    # 将除2取余的结果添加到列表中
    num_10 = int(num_10 / 2)    # 将十进制数除以2

print("".join(map(str, num_2[::-1])))
