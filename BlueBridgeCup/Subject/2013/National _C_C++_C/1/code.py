#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/30 H:05
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
import itertools

if __name__ == '__main__':
    count, ans, s = 0, 0, ['好', '好', '学', '习']
    for item in list(itertools.permutations(s)):
        count += 1
        if "".join(item) == "好好学习":
            ans += 1
    print(f"{ans} / {count}")
