#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/1/29 19:07
# @File     : 1.XOR_swap.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import random

a = random.randint(0, 100)
b = random.randint(0, 100)
print("a = ", a, " b = ", b)
a = a ^ b
b = a ^ b
a = a ^ b
print("a = ", a, " b = ", b)
