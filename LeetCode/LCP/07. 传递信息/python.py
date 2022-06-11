# -*- coding: utf-8 -*-
# @Author   : Alex
# @Time     : 2022/6/10 8:14
# @File     : python.py
# @Software : PyCharm
# Email     : liu_zhao_feng_alex@163.com
# Blog      : https://alex007.blog.csdn.net/
from typing import List


class Solution:
	def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
		def dfs(idx, depth):
			if depth > k:
				return
			if depth == k and idx == n - 1:
				nonlocal ans
				ans += 1
			for target in adjacency.get(idx, []):
				dfs(target, depth + 1)
		
		adjacency = {}
		for (start, end) in relation:
			if adjacency.get(start, None):
				adjacency[start].append(end)
			else:
				adjacency[start] = [end]
		
		ans = 0
		dfs(0, 0)
		return ans


if __name__ == '__main__':
	print(Solution().numWays(n=5, relation=[[0, 2], [2, 1], [3, 4], [2, 3], [1, 4], [2, 0], [0, 4]], k=3))
