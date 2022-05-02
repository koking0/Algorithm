#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/1/29 19:24
# @File     : B.Odd_Times_Num1.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import copy
import random


def odd_times_num1(array):
    eor = 0
    for num in array:
        eor = eor ^ num
    return eor


if __name__ == '__main__':
    length = random.randint(0, 10)
    array1 = [random.randint(0, 100) for _ in range(length)]
    array2 = copy.deepcopy(array1)
    array3 = array1 + array2
    array3.insert(random.randint(0, length), random.randint(0, 100))
    print(array3)
    print(odd_times_num1(array3))
