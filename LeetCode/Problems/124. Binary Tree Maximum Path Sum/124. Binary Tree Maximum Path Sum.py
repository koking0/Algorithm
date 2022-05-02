#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/6/21 7:40
# @File     : 124. Binary Tree Maximum Path Sum.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def __init__(self):
		self.maxSum = float("-inf")

	def maxPathSum(self, root: TreeNode) -> int:
		def maxGain(node: TreeNode):
			if not node:
				return 0
			leftGain = max(maxGain(node.left), 0)
			rightGain = max(maxGain(node.right), 0)
			priceNewPath = node.val + leftGain + rightGain
			self.maxSum = max(self.maxSum, priceNewPath)
			return node.val + max(leftGain, rightGain)

		maxGain(root)
		return self.maxSum
