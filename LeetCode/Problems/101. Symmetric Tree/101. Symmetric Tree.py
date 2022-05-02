#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/5/31 9:19
# @File     : 101. Symmetric Tree.py
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
	def isSymmetric_D(self, root: TreeNode) -> bool:
		def check(p: TreeNode, q: TreeNode):
			if p is None and q is None:
				return True
			if p is None or q is None:
				return False
			return p.val == q.val and check(p.left, q.right) and check(p.right, q.left)

		return check(root, root)

	def isSymmetric_B(self, root: TreeNode) -> bool:
		def check(x: TreeNode, y: TreeNode):
			from queue import Queue
			q = Queue()
			q.put(x)
			q.put(y)
			while not q.empty():
				u = q.get()
				v = q.get()
				if not u and not v:
					continue
				if (not u or not v) or (u.val != v.val):
					return False
				q.put(u.left)
				q.put(v.right)
				q.put(u.right)
				q.put(v.left)
			return True

		return check(root, root)
