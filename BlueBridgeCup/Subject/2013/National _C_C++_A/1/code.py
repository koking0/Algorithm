#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/22 9:44
# @File     : code.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> WeChat    : Alex-Paddle
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import itertools

if __name__ == '__main__':
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for item in itertools.permutations(numbers):
        ABCD = item[0] * 1000 + item[1] * 100 + item[2] * 10 + item[3]
        EFGH = item[4] * 1000 + item[5] * 100 + item[6] * 10 + item[7]
        XY = item[8] * 10 + item[9]
        if (ABCD - EFGH) * XY == 900:
            print(f'({ABCD} - {EFGH}) * {XY} = 900')
