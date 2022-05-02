#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/B/12 10:57
# @File     : BubbleSortCode.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import itertools

num = [2, 4, 5, 6, 7, 9, 10, 11, 12]
for solve in list(itertools.permutations(num, len(num))):
    solve = list(solve)
    solve.insert(0, 1)
    solve.insert(1, 8)
    solve.insert(11, 3)
    if solve[0] + solve[2] + solve[5] + solve[7] == \
       solve[1] + solve[2] + solve[3] + solve[4] == \
       solve[0] + solve[3] + solve[6] + solve[10] == \
       solve[1] + solve[5] + solve[8] + solve[11] == \
       solve[4] + solve[6] + solve[9] + solve[11] == \
       solve[7] + solve[8] + solve[9] + solve[10]:
        print(solve)
