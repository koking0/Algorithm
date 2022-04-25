#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/H/H 9:01
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
	def recoverTree(self, root: TreeNode) -> None:
		"""
        Do not return anything, modify root in-place instead.
        """
		Trees = lambda x: [] if not x else Trees(x.left) + [x] + Trees(x.right)
		a = Trees(root)
		sa = sorted(a, key=lambda x: x.val)
		temp = [a[i] for i in range(len(a)) if a[i] != sa[i]]
		temp[0].val, temp[1].val = temp[1].val, temp[0].val
