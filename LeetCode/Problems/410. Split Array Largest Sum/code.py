#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/25 H:08
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
import sys
from typing import List


class Solution:
	def splitArray(self, nums: List[int], m: int) -> int:
		length, subSum = len(nums), [0]
		dp = [[sys.maxsize for _ in range(m + 1)] for _ in range(length + 1)]
		dp[0][0] = 0
		for element in nums:
			subSum.append(subSum[-1] + element)

		for i in range(1, length + 1):
			for j in range(1, min(i, m) + 1):
				for k in range(i):
					dp[i][j] = min(dp[i][j], max(dp[k][j - 1], subSum[i] - subSum[k]))
		return dp[length][m]
