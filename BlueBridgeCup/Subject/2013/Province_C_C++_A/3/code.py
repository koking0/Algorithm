#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/31 H:18
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


def dfs(x, y):
    if x == 3 and y == 4:
        global ans
        ans += 1
        return

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 4 and 0 <= ny < 5:
            dfs(nx, ny)


if __name__ == '__main__':
    ans, dirs = 0, [(1, 0), (0, 1)]
    dfs(0, 0)
    print(ans)
