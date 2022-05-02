#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/B/11 18:40
# @File     : BubbleSortCode.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
"""
枚举四个数a、b、c、d分别从0~9，并且各不相同

然后组合为ab * cd和a * bcd计算出结果转换为字符串然后排序看是否与abcd相同
"""


def check(num1, num2):
    num1 = list(map(int, str(num1)))
    num2 = list(map(int, str(num2)))
    num1.sort()
    num2.sort()
    return num1 == num2


count = 0
for a in range(1, 10):
    for b in range(10):
        if b != a:
            for c in range(10):
                if c != a and c != b:
                    for d in range(10):
                        if d != a and d != b and d != c:
                            target = a * 1000 + b * 100 + c * 10 + d
                            product1 = (a * 10 + b) * (c * 10 + d)
                            product2 = a * (b * 100 + c * 10 + d)

                            if check(target, product1) and (a * 10 + b) < (c * 10 + d):
                                print((a * 10 + b), "*", (c * 10 + d), "=", (a * 10 + b) * (c * 10 + d))
                                count += 1
                            if check(target, product2):
                                print(a, "*", (b * 100 + c * 10 + d), "=", a * (b * 100 + c * 10 + d))
                                count += 1
print(count)
