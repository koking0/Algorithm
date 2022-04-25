#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/H/11 H:09
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
from typing import List


class Solution:
	def solve(self, board: List[List[str]]) -> None:
		"""
        Do not return anything, modify board in-place instead.
        """
		if not board:
			return

		def dfs(x, y):
			if not 0 <= x < rows or not 0 <= y < cols or board[x][y] != 'O':
				return

			board[x][y] = 'V'
			dfs(x + 1, y)
			dfs(x - 1, y)
			dfs(x, y + 1)
			dfs(x, y - 1)

		rows, cols = len(board), len(board[0])

		for r in range(rows):
			dfs(r, 0)
			dfs(r, cols - 1)
		for c in range(1, cols - 1):
			dfs(0, c)
			dfs(rows - 1, c)
		for r in range(rows):
			for c in range(cols):
				if board[r][c] == 'V':
					board[r][c] = 'O'
				elif board[r][c] == 'O':
					board[r][c] = 'X'
