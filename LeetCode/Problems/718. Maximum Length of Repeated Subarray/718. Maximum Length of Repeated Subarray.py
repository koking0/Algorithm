#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/1 7:34
# @File     : 718. Maximum Length of Repeated Subarray.py
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
	def findLength_violence(self, A: List[int], B: List[int]) -> int:
		lengthA, lengthB, ans = len(A), len(B), 0
		for i in range(lengthA):
			for j in range(lengthB):
				k = 0
				while i + k < lengthA and j + k < lengthB and A[i + k] == B[j + k]:
					k += 1
				ans = max(ans, k)
		return ans

	def findLength_dynamicProgramming(self, A: List[int], B: List[int]) -> int:
		ans, lengthA, lengthB = 0, len(A), len(B)
		dp = [[0] * (lengthB + 1) for _ in range(lengthA + 1)]
		for i in range(lengthA - 1, -1, -1):
			for j in range(lengthB - 1, -1, -1):
				dp[i][j] = dp[i + 1][j + 1] + 1 if A[i] == B[j] else 0
				ans = max(ans, dp[i][j])
		return ans


