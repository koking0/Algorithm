#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/6/17 7:47
# @File     : 1014. Best Sightseeing Pair.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
from typing import List


class Solution:
	def maxScoreSightseeingPair_violence(self, A: List[int]) -> int:
		length, ans = len(A), 0
		for i in range(length):
			for j in range(i + 1, length):
				ans = max(ans, A[i] + A[j] + i - j)
		return ans

	def maxScoreSightseeingPair(self, A: List[int]) -> int:
		ans, mx = 0, A[0] + 0
		for j in range(1, len(A)):
			ans = max(ans, mx + A[j] - j)
			mx = max(mx, A[j] + j)
		return ans
