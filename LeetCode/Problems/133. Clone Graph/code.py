#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/H/12 9:23
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


# Definition for a Node.
class Node:
	def __init__(self, val=0, neighbors=[]):
		self.val = val
		self.neighbors = neighbors


class Solution:
	def __init__(self):
		self.visited = {}

	def cloneGraph(self, node: 'Node') -> 'Node':
		if not node:
			return node

		if node in self.visited:
			return self.visited[node]

		cloneNode = Node(node.val, [])
		self.visited[node] = cloneNode
		if node.neighbors:
			cloneNode.neighbors = [self.cloneGraph(n) for n in node.neighbors]
		return cloneNode
