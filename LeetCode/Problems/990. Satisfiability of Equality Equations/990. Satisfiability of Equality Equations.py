#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/6/H 7:34
# @File     : 990. Satisfiability of Equality Equations.py
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

	class UnionFind:
		def __init__(self):
			self.parent = list(range(26))

		def find(self, index):
			if index == self.parent[index]:
				return index
			self.parent[index] = self.find(self.parent[index])
			return self.parent[index]

		def union(self, index1, index2):
			self.parent[self.find(index1)] = self.find(index2)

	def equationsPossible(self, equations: List[str]) -> bool:
		uf = Solution.UnionFind()
		for item in equations:
			if item[1] == '=':
				index1 = ord(item[0]) - ord("a")
				index2 = ord(item[3]) - ord("a")
				uf.union(index1, index2)
		for item in equations:
			if item[1] == '!':
				index1 = ord(item[0]) - ord("a")
				index2 = ord(item[3]) - ord("a")
				if uf.find(index1) == uf.find(index2):
					return False
		return True
