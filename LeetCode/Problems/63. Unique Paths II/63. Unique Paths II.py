#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/6 H:14
# @File     : 63. Unique Paths II.py
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
	def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
		rows, cols = len(obstacleGrid), len(obstacleGrid[0])
		dp = [1] + [0] * cols
		for i in range(0, rows):
			for j in range(0, cols):
				dp[j] = 0 if obstacleGrid[i][j] else dp[j] + dp[j - 1]
		return dp[-2]
