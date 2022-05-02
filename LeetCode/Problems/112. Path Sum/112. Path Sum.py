#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/7 H:20
# @File     : 112. Path Sum.py
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
	def hasPathSum(self, root: TreeNode, sum: int) -> bool:
		if not root:
			return False
		if not root.left and not root.right:
			return sum == root.val
		return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
