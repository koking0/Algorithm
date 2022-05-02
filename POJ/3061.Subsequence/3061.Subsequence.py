#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/1/28 16:27
# @File     : 3061.Subsequence.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import sys

while True:
    try:
        length, target = map(int, input().split())
        sequence = list(map(int, input().split()))
        left, sum_num, ans = 0, 0, sys.maxsize
        for right in range(length):
            sum_num += sequence[right]
            while sum_num > target:
                ans = min(right - left + 1, ans)

                sum_num -= sequence[left]
                left += 1
        print(ans if ans != sys.maxsize else 0)
    except EOFError:
        break
