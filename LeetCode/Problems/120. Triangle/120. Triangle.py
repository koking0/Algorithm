#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/14 7:47
# @File     : 120. Triangle.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import sys
from typing import List


class Solution:
	def minimumTotal(self, triangle: List[List[int]]) -> int:
		for i in range(len(triangle) - 2, -1, -1):
			for j in range(len(triangle[i])):
				triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
		return triangle[0][0]
