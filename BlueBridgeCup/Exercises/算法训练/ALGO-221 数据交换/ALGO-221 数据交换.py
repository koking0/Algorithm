#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/6/23 7:52
# @File     : ALGO-221 数据交换.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


def swap(a, b):
    return b, a


if __name__ == '__main__':
    a, b = input().split(" ")
    a, b = swap(a, b)
    print(a, b)
