#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/H/B 9:01
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


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def flatten(self, root: TreeNode) -> None:
		"""
        Do not return anything, modify root in-place instead.
        """
		def preOrderTraversal(root: TreeNode):
			if root:
				preOrderList.append(root)
				preOrderTraversal(root.left)
				preOrderTraversal(root.right)

		preOrderList = []
		preOrderTraversal(root)
		size = len(preOrderList)
		for i in range(1, size):
			prev, curr = preOrderList[i - 1], preOrderList[i]
			prev.left = None
			prev.right = curr
