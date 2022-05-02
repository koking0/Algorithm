#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/6/3 5:22
# @File     : 837. New 21 Game.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


class Solution:
	def new21Game(self, N: int, K: int, W: int) -> float:
		if K == 0:
			return 1.0
		dp = [0.0] * (K + W + 1)
		for i in range(K, min(N, K + W - 1) + 1):
			dp[i] = 1.0
		dp[K - 1] = float(min(N - K + 1, W) / W)
		for i in range(K - 2, -1, -1):
			dp[i] = dp[i + 1] - (dp[i + W + 1] - dp[i + 1]) / W
		return dp[0]
