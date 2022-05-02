#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/21 H:53
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


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def generateTrees(self, n: int) -> List[TreeNode]:
		memory = {}

		def generateTree(start, end):
			nonlocal memory
			if (start, end) in memory:
				return memory[start, end]
			if start > end:
				return [None, ]
			allTrees = []
			for i in range(start, end + 1):
				leftTrees = generateTree(start, i - 1)
				rightTrees = generateTree(i + 1, end)
				for j in leftTrees:
					for k in rightTrees:
						currentTree = TreeNode(i)
						currentTree.left = j
						currentTree.right = k
						allTrees.append(currentTree)
			memory[start, end] = allTrees
			return allTrees

		return generateTree(1, n) if n else []


a = Solution()
a.generateTrees(3)
