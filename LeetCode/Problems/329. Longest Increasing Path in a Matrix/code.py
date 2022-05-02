#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/26 7:59
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
from functools import lru_cache
from typing import List


class Solution:
	def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
		if not matrix:
			return 0

		rows, cols, ans = len(matrix), len(matrix[0]), 0
		dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

		@lru_cache(None)
		def dfs(x, y):
			best = 1
			for dx, dy in dirs:
				nx, ny = x + dx, y + dy
				if -1 < nx < rows and -1 < ny < cols and matrix[nx][ny] > matrix[x][y]:
					best = max(best, dfs(nx, ny) + 1)
			return best

		for r in range(rows):
			for c in range(cols):
				ans = max(ans, dfs(r, c))
		return ans


so = Solution()
print(so.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
