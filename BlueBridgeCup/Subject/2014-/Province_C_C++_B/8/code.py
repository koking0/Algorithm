#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/B/12 11:20
# @File     : BubbleSortCode.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
"""
当两只蚂蚁碰面时，它们会同时掉头往相反的方向爬行，可以理解为穿过。

感冒蚂蚁向右：
    在感冒蚂蚁右边的蚂蚁：
        向右——》不会被传染
        向左——》会被传染
    在感冒蚂蚁左边的蚂蚁：
        向右——》感冒蚂蚁右边有向左的蚂蚁会被传染，否则不会被传染
        向左——》不会被传染

感冒蚂蚁向左：
    在感冒蚂蚁左边的蚂蚁：
        向右——》会被传染
        向左——》不会被传染
    在感冒蚂蚁右边的蚂蚁：
        向右——》不会被传染
        向左——》感冒蚂蚁左边有向右的蚂蚁会被传染，否则不会被传染

总结：
    在感冒蚂蚁前进路上且方向相反的蚂蚁会被传染
    在感冒蚂蚁相反路上但前进方向与感冒蚂蚁相同的蚂蚁如果上一个条件有被传染的蚂蚁则全被传染否则不会被传染
"""
count = 1
_ = int(input())
nums = list(map(int, input().split()))
if nums[0] > 0:
    for i in nums:
        if nums[0] * i < 0 and abs(i) > abs(nums[0]):
            count += 1
    for i in nums:
        if count > 1 and abs(i) < abs(nums[0]) and nums[0] * i > 0:
            count += 1
if nums[0] < 0:
    for i in nums:
        if nums[0] * i < 0 and abs(i) < abs(nums[0]):
            count += 1
    for i in nums:
        if count > 1 and abs(i) > abs(nums[0]) and nums[0] * i > 0:
            count += 1
print(count)
