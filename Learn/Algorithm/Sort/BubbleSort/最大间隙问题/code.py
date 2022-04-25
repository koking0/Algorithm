#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/1/19 下午7:06
# @File     : BubbleSortCode.py
# @Project  : Algorithm
# @Software : PyCharm
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
#
# 最大间隙问题：给定n个实数x1, x2 ,..., xn，求这n个数在实轴上相邻2个数之间的最大差值。
# 假设对任何实数的下取整函数耗O(1)，设计解最大间隙问题的线性时间算法。
import copy
import random


def max_gap(arr: list):
    if len(arr) < 2:
        return 0
    min_value = min(arr)
    max_value = max(arr)
    if min_value == max_value:
        return 0
    min_values = [100] * (len(arr) + 1)
    max_values = [0] * (len(arr) + 1)
    have_num = [False] * (len(arr) + 1)
    for temp in range(len(arr)):
        bid = bucket(arr[temp], len(arr), min_value, max_value)
        have_num[bid] = True
        max_values[bid] = max(max_values[bid], arr[temp]) if have_num[bid] else arr[temp]
        min_values[bid] = min(min_values[bid], arr[temp]) if have_num[bid] else arr[temp]
    res = 0
    last_max = max_values[0]
    for temp in range(1, len(arr) + 1):
        if have_num[temp]:
            res = max(res, min_values[temp] - last_max)
            last_max = max_values[temp]
    return res


def bucket(num, arr_len, min_value, max_value):
    return int((num - min_value) * arr_len / (max_value - min_value))


def solve(arr: list):
    if len(arr) < 2:
        return 0

    ans = 0
    arr.sort()
    for temp in range(1, len(arr)):
        ans = max(arr[temp] - arr[temp - 1], ans)
    return ans


if __name__ == '__main__':
    flag = True
    for i in range(1000):
        list1 = [random.randint(0, 100) for _ in range(random.randint(0, 10))]
        list2 = copy.deepcopy(list1)
        list3 = copy.deepcopy(list1)
        res1 = max_gap(list2)
        res2 = solve(list3)
        if res1 != res2:
            flag = False
            list1.sort()
            print('list 1 = ', list1)
            print(res1)
            print(res2)
            break

    print('Nice' if flag else 'Fuck')
