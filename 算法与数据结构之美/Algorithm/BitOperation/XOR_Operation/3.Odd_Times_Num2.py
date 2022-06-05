#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/1/29 19:31
# @File     : 3.Odd_Times_Num2.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import copy
import random


def odd_times_num2(array):
    eor1 = 0
    for num in array:
        eor1 = eor1 ^ num

    cur, eor2 = eor1 & (~eor1 + 1), 0
    for num in array:
        if cur & num:
            eor2 = eor2 ^ num
    return eor1 ^ eor2, eor2


if __name__ == '__main__':
    length = random.randint(0, 10)
    array1 = [random.randint(0, 100) for _ in range(length)]
    array2 = copy.deepcopy(array1)
    array3 = array1 + array2
    array3.insert(random.randint(0, length), random.randint(0, 100))
    array3.insert(random.randint(0, length), random.randint(0, 100))
    print(array3)
    print(odd_times_num2(array3))
