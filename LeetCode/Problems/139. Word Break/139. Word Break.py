#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/6/25 7:59
# @File     : 139. Word Break.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        if not wordDict:
            return not s
        dp = [False] * (length + 1)
        dp[0] = True
        for i in range(1, length + 1):
            for j in range(i - 1, -1, -1):
                if dp[j] and s[j: i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
