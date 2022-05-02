#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/29 7:46
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
from collections import deque
from typing import List


class Solution:
	def minimalSteps(self, maze: List[str]) -> int:
		def bfs(x, y):
			ret = [[float('inf') for _ in range(cols)] for _ in range(rows)]
			ret[x][y], queue = 0, deque([x, y])
			while queue:
				x, y, d = queue.popleft()
				for dx, dy in dirs:
					nx, ny = x + dx, y + dy
					if 0 <= nx < rows and 0 <= ny < cols:
						if maze[nx][ny] != '#' and d + 1 < ret[nx][ny]:
							ret[nx][ny] = d + 1
							queue.append((nx, ny, d + 1))
			return ret

		buttons, stones = [], []
		sx, sy, tx, ty = 0, 0, 0, 0
		rows, cols = len(maze), len(maze[0])
		dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
		for i in range(rows):
			for j in range(cols):
				if maze[i][j] == 'M':
					buttons.append((i, j))
				if maze[i][j] == 'O':
					stones.append((i, j))
				if maze[i][j] == 'S':
					sx, sy = i, j
				if maze[i][j] == 'T':
					tx, ty = i, j

		lenb, lens = len(buttons), len(stones)
		startDist = bfs(sx, sy)
