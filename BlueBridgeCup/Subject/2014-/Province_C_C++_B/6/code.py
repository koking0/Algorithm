#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/B/12 10:41
# @File     : BubbleSortCode.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
"""
(a / b) * (c / d) = (ac / bd)
可以化简为：
a * c * bd = ac * b * d
"""
count = 0
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a != b and c != d and a * c * (b * 10 + d) == (a * 10 + c) * b * d:
                    count += 1
                    print("(%d / %d) * (%d / %d) = (%d / %d)" % (a, b, c, d, a * 10 + c, b * 10 + d))
print(count)
