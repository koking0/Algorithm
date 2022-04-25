#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/H/16 H:22
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
	def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
		def dfs(x, y):
			if not (-1 < x < len(image) and -1 < y < len(image[0]) and image[x][y] == oldColor):
				return
			image[x][y] = newColor
			for dx, dy in dirs:
				nx, ny = x + dx, y + dy
				dfs(nx, ny)

		dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
		oldColor = image[sr][sc]
		if oldColor != newColor:
			dfs(sr, sc)
		return image
