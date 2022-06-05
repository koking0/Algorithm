#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/B/11 12:41
# @File     : M_to_N.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import string


m = int(input("M = "))
num_m = input("M number = ")
n = int(input("N = "))

num_10 = 0
num_m = list(num_m.upper())
for i in range(len(num_m)):
    if num_m[i].isalpha():     # 如果当前元素为字母
        num_m[i] = ord(num_m[i]) - ord("A") + 10  # 转换为相应的数字

for i in range(len(num_m)):     # 明确循环次数的时候用for循环
    num_10 += int(num_m[::-1][i]) * (m ** i)

num_n = []      # 其他语言可以用数组
while num_10:     # 不明确循环次数的时候用while循环
    num_n.append(num_10 % n)  # 将除2取余的结果添加到列表中
    num_10 = int(num_10 / n)    # 将十进制数除以2

char = list(string.ascii_uppercase)         # 26大写英文字母集
for i in range(len(num_n)):
    if num_n[i] > 9:                      # 如果数字大于两位
        num_n[i] = char[num_n[i] - 10]  # 转换为相应的字母
print("N number =", "".join(map(str, num_n[::-1])))
