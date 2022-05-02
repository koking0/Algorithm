#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/1/12 下午11:10
# @Author   : alex
# @File     : BubbleSortCode.py
# @Project  : Algorithm
# @Software : PyCharm

# 在一个数组中，每一个数左边比当前数小的数累加起来，叫做这个数组的小和。


import copy
import random


def small_sum1(arr: list):
    return mergeSort(arr, 0, len(arr) - 1)


def mergeSort(arr: list, left: int, right: int):
    if left == right:
        return 0
    mid = left + ((right - left) >> 1)
    return mergeSort(arr, left, mid) + mergeSort(arr, mid + 1, right) + merge(arr, left, mid, right)


def merge(arr: list, left: int, mid: int, right: int):
    help_list = []
    p1, p2, res = left, mid + 1, 0

    while p1 <= mid and p2 <= right:
        if arr[p1] < arr[p2]:
            res += arr[p1] * (right - p2 + 1)
            help_list.append(arr[p1])
            p1 += 1
        else:
            help_list.append(arr[p2])
            p2 += 1

    while p1 <= mid:
        help_list.append(arr[p1])
        p1 += 1

    while p2 <= right:
        help_list.append(arr[p2])
        p2 += 1

    for j in range(len(help_list)):
        arr[left + j] = help_list[j]

    return res


def small_sum2(arr: list):
    res = 0
    for temp in range(1, len(arr)):
        for j in range(0, temp):
            res += arr[j] if arr[j] < arr[temp] else 0
    return res


def generate_random_test(max_size: int, max_value: int):
    result = []
    size = random.randint(0, max_size + 1)
    for i in range(size):
        result.append((int((max_value + 1) * random.random())) - int((max_value * random.random())))
    return result


if __name__ == '__main__':
    test_num = 10
    max_size = 10
    max_value = 100
    flag = True

    for i in range(test_num):
        list1 = generate_random_test(max_size, max_value)
        list2 = copy.deepcopy(list1)
        list3 = copy.deepcopy(list1)
        res1 = small_sum1(list2)
        res2 = small_sum2(list3)
        if res1 != res2:
            flag = False
            print(list1)
            print(list2)
            print(list3)
            break

    print("Nice" if flag else "Fuck")
