#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/7 10:58
# @File     : 1006.最长公共子序列Lcs.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


def Lcs(str1: str, str2: str):
    length1, length2 = len(str1), len(str2)
    dp = [['' for _ in range(length2 + 1)] for _ in range(length1 + 1)]
    for i in range(length1):
        for j in range(length2):
            if str1[i] == str2[j]:
                dp[i + 1][j + 1] = dp[i][j] + str1[i]
            elif len(dp[i + 1][j]) > len(dp[i][j + 1]):
                dp[i + 1][j + 1] = dp[i + 1][j]
            else:
                dp[i + 1][j + 1] = dp[i][j + 1]
    return dp[-1][-1]


if __name__ == '__main__':
    print(Lcs(input(), input()))
