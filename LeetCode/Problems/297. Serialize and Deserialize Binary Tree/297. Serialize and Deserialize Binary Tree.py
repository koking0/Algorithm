#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/6/16 H:03
# @File     : 297. Serialize and Deserialize Binary Tree.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import collections


# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Codec:

	def serialize(self, root):
		"""Encodes a tree to a single string.

		:type root: TreeNode
		:rtype: str
		"""
		if not root:
			return "[]"

		res, queue = [], collections.deque()
		queue.append(root)
		while queue:
			node = queue.popleft()
			if node:
				res.append(str(node.val))
				queue.append(node.left)
				queue.append(node.right)
			else:
				res.append("null")
		return f"[{','.join(res)}]"

	def deserialize(self, data):
		"""Decodes your encoded data to tree.

		:type data: str
		:rtype: TreeNode
		"""
		if data == "[]":
			return None

		values, index = data[1: -1].split(","), 1
		root = TreeNode(int(values[0]))
		queue = collections.deque()
		queue.append(root)
		while queue:
			node = queue.popleft()
			if values[index] != "null":
				node.left = TreeNode(int(values[index]))
				queue.append(node.left)
			index += 1
			if values[index] != "null":
				node.right = TreeNode(int(values[index]))
				queue.append(node.right)
			index += 1
		return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
