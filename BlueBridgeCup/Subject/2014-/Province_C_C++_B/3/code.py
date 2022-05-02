#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/B/11 19:54
# @File     : BubbleSortCode.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


def dfs(wine, store, flower):
    if wine == 1 and store == 0 and flower == 1:
        return 1
    if store < 0 or flower < 0:
        return 0
    return dfs(wine * 2, store - 1, flower) + dfs(wine - 1, store, flower - 1)


print(dfs(2, 5, 10))
