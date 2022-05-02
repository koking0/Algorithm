#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/5/22 11:00
# @File     : 105. Construct Binary Tree from Preorder and Inorder Traversal.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
from typing import List


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
		def buildTree(preOrderLeft: int, preOrderRight: int, inOrderLeft: int, inOrderRight: int):
			if preOrderLeft > preOrderRight:
				return None

			preRootIndex = preOrderLeft
			inRootIndex = index[preorder[preRootIndex]]

			root = TreeNode(preorder[preRootIndex])
			leftSubTreeLength = inRootIndex - inOrderLeft

			root.left = buildTree(preOrderLeft + 1, preOrderLeft + leftSubTreeLength, inOrderLeft, inRootIndex - 1)
			root.right = buildTree(preOrderLeft + leftSubTreeLength + 1, preOrderRight, inRootIndex + 1, inOrderRight)
			return root

		length = len(preorder)
		index = {value: key for key, value in enumerate(inorder)}
		return buildTree(0, length - 1, 0, length - 1)
