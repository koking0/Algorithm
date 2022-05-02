#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/7 9:07
# @File     : code.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


def Lcs1(str1: str, str2: str):
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(n):
            dp[i + 1][j + 1] = 1 + dp[i][j] if str1[i] == str2[j] else max(dp[i][j + 1], dp[i + 1][j])
    print(dp)
    return dp


def Lcs2(str1: str, str2: str):
    cur, dp = 1, [[0 for _ in range(n + 1)] for _ in range(2)]
    for i in range(n):
        cur = abs(cur - 1)
        pre = abs(cur - 1)
        for j in range(n):
            dp[pre][j + 1] = 1 + dp[cur][j] if str1[i] == str2[j] else max(dp[cur][j + 1], dp[pre][j])
    return dp


if __name__ == '__main__':
    n = int(input())
    p1 = input().strip(' ')
    p2 = input().strip(' ')
    print(Lcs2(p1, p2)[-1][-1])
