#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/H/4 9:13
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
import collections
from typing import List


class Solution:
	def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
		def dfs(u: int):
			nonlocal valid
			visited[u] = 1
			for v in edges[u]:
				if visited[v] == 0:
					dfs(v)
					if not valid:
						return
				elif visited[v] == 1:
					valid = False
					return
			visited[u] = 2
			result.append(u)

		edges = collections.defaultdict(list)
		visited, result, valid = [0] * numCourses, list(), True

		for info in prerequisites:
			edges[info[1]].append(info[0])

		for i in range(numCourses):
			if valid and not visited[i]:
				dfs(i)

		return valid
