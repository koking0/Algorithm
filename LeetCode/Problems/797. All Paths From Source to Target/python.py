# -*- coding: utf-8 -*-
# @Time        : 2022/2/28 20:21
# @File        : python.py
# @Description : None
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> Mail      : liu_zhao_feng_alex@163.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
from typing import List
from copy import deepcopy


class Solution:
	def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
		def dfs(node, path):
			if node == n - 1:
				ans.append(deepcopy(path + [node]))
				return

			for next_node in graph[node]:
				if next_node not in path:
					path.append(node)
					dfs(next_node, path)
					path.pop()

		n = len(graph)
		ans = []
		dfs(0, [])
		return ans


if __name__ == '__main__':
	print(Solution().allPathsSourceTarget(graph=[[4, 3, 1], [3, 2, 4], [3], [4], []]))
