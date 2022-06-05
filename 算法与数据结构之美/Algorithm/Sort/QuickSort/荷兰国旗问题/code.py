# !/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/1/14 下午8:41
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
# 给定一个数组arr，和一个数num，把小于num的数放在数组左边，等与num的数放在数组的中间，大于num的数放在数组的右边，要求额外空间复杂度O(1)，时间复杂度O(N)。
import random


def partition(arr: list, left: int, right: int, num: int):
    less = left - 1
    more = right + 1
    while left < more:
        if arr[left] < num:
            less += 1
            arr[less], arr[left] = arr[less], arr[left]
            left += 1
        elif arr[left] > num:
            more -= 1
            arr[more], arr[left] = arr[left], arr[more]
        else:
            left += 1
    return less + 1, more - 1


def generate_list():
    return [random.randint(0, 2) for _ in range(10)]


if __name__ == "__main__":
    test = generate_list()
    print(test, partition(test, 0, 9, 1))
