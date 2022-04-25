#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/1/29 23:14
# @File     : B. Infinite Prefixes.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


for _ in range(int(input())):
    n, x = map(int, input().split())
    s = input()

    y = s.count('0') - s.count('1')
    z, ans, inf = 0, 0, False

    if x == 0:
        ans = 1
    for i in s:
        z += (i == '0') - (i == '1')
        if y == 0 and z == x:
            # 如果字符串中0和1的个数相等
            inf = True
            print(-1)
            break
        if x - z == 0 or ((x - z) * y > 0 and (x - z) % y == 0):
            ans += 1
    if not inf:
        print(ans)
