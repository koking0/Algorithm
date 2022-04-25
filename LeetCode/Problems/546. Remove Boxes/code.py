#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/H/15 7:54
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


class Solution:
	def removeBoxes(self, boxes: List[int]) -> int:
		def dp(l, r, n):
			nonlocal memo, boxes
			if memo.get((l, r, n)):
				return memo[(l, r, n)]

			if l == r - 1:
				return (n + 1) * (n + 1)

			if boxes[l] == boxes[l + 1]:
				return dp(l + 1, r, n + 1)

			res = (n + 1) * (n + 1) + dp(l + 1, r, 0)
			for l2 in range(l + 2, r):
				if boxes[l2] == boxes[l]:
					res = max(res, dp(l + 1, l2, 0) + dp(l2, r, n + 1))
			memo[(l, r, n)] = res
			return res

		memo = {}
		return dp(0, len(boxes), 0)
