#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/12 H:35
# @File     : 174. Dungeon Game.py
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
	def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
		rows, cols = len(dungeon), len(dungeon[0])
		dp = [[10 ** 9] * (cols + 1) for _ in range(rows + 1)]
		dp[rows][cols -1] = dp[rows - 1][cols] = 1
		for i in range(rows - 1, -1, -1):
			for j in range(cols - 1, -1, -1):
				minn = min(dp[i + 1][j], dp[i][j + 1])
				dp[i][j] = max(minn - dungeon[i][j], 1)
		return dp[0][0]
