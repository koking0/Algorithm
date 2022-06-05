#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/B/11 11:54
# @File     : 10_to_any.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import string


num_10 = int(input("输入的十进制数:"))
base = int(input("输入要转换为的进制:"))
num_any = []      # 其他语言可以用数组

while num_10:     # 不明确循环次数的时候用while循环
    num_any.append(num_10 % base)  # 将除2取余的结果添加到列表中
    num_10 = int(num_10 / base)    # 将十进制数除以2

char = list(string.ascii_uppercase)         # 26大写英文字母集
for i in range(len(num_any)):
    if num_any[i] > 9:                      # 如果数字大于两位
        num_any[i] = char[num_any[i] - 10]  # 转换为相应的字母
print("".join(map(str, num_any[::-1])))
