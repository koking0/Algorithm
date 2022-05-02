#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/H/5 9:04
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
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def rob(self, root: TreeNode) -> int:
		def _rob(r):
			if not r:
				return 0, 0
			ls, ln = _rob(r.left)
			rs, rn = _rob(r.right)
			return r.val + ln + rn, max(ls, ln) + max(rs, rn)
		return max(_rob(root))
