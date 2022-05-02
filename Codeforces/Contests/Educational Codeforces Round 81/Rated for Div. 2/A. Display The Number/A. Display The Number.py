#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/1/29 22:38
# @File     : A. Display The Number.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


for _ in range(int(input())):
    n = int(input())
    print("7" + "1" * ((n - 3) // 2) if n % 2 else "1" * (n // 2))
