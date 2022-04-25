#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/19 H:43
# @File     : 312. Burst Balloons.py
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
	def maxCoins(self, nums: List[int]) -> int:
		length, val = len(nums), [1] + nums + [1]
		dp = [[0] * (length + 2) for _ in range(length + 2)]

		for i in range(length - 1, -1, -1):
			for j in range(i + 2, length + 2):
				for k in range(i + 1, j):
					total = val[i] * val[k] * val[j]
					total += dp[i][k] + dp[k][j]
					dp[i][j] = max(dp[i][j], total)
		return dp[0][length + 1]
