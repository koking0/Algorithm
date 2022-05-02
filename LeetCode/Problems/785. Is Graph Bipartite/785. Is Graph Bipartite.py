#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/16 H:31
# @File     : 785. Is Graph Bipartite.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import collections
from typing import List


class Solution:
	def isBipartite_DFS(self, graph: List[List[int]]) -> bool:
		n, unColored, red, green = len(graph), 0, 1, 2
		color, valid = [unColored] * n, True

		def dfs(node: int, c: int):
			nonlocal valid
			color[node] = c
			nextC = (green if c == red else red)
			for neighbor in graph[node]:
				if color[neighbor] == unColored:
					dfs(neighbor, nextC)
					if not valid:
						return
				elif color[neighbor] != nextC:
					valid = False
					return

		for i in range(n):
			if color[i] == unColored:
				dfs(i, red)
				if not valid:
					break
		return valid

	def isBipartite_BFS(self, graph: List[List[int]]) -> bool:
		n, unColored, red, green = len(graph), 0, 1, 2
		color = [unColored] * n

		for i in range(n):
			if color[i] == unColored:
				q = collections.deque([i])
				color[i] = red
				while q:
					node = q.popleft()
					nextC = (green if color[node] == red else red)
					for neighbor in graph[node]:
						if color[neighbor] == unColored:
							q.append(neighbor)
							color[neighbor] = nextC
						elif color[neighbor] != nextC:
							return False
		return True
