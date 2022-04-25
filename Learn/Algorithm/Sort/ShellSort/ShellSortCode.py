#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/4/17 22:27
# @File     : BubbleSortCode.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import copy
import random


def shellSort(array: list):
    length, gap = len(array), len(array) // 2
    while gap > 0:
        for trip in range(gap, length):
            for index in range(trip - gap, -1, -gap):
                if array[index] > array[index + gap]:
                    array[index], array[index + gap] = array[index + gap], array[index]
        gap //= 2


if __name__ == '__main__':
    flag = True
    for i in range(1):
        list1 = [random.randint(0, 100) for _ in range(random.randint(0, 5))]
        list2 = copy.deepcopy(list1)
        list3 = copy.deepcopy(list1)
        shellSort(list2)
        list3.sort()
        if list2 != list3:
            flag = False
            print(list1)
            print(list2)
            print(list3)
            break
    print("Nice" if flag else "Fuck")
