#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/B/11 18:35
# @File     : BubbleSortCode.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
for i in range(1, 100):
    if not (i & 1):        # 填空
        print(int(i * i / 2), end=" ")
    else:
        print(int((i * i-1) / 2), end=" ")
print()
