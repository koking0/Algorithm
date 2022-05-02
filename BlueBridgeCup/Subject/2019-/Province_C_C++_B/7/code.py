#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/20 11:08
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
if __name__ == '__main__':
    maxNum, sumNum, maxIndex, nowIndex = 0, 0, 1, 1
    N = int(input())
    nums = list(map(int, input().split(' ')))
    for i, value in enumerate(nums):
        index = 2 ** nowIndex - 1
        if i > index:
            maxIndex = maxIndex if maxNum > sumNum else nowIndex
            maxNum = maxNum if maxNum > sumNum else sumNum
            nowIndex += 1
            sumNum = 0
        sumNum += value
    print(maxIndex)
