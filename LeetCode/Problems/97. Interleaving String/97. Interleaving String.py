#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/18 9:49
# @File     : 97. Interleaving String.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


class Solution:
	def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
		length1, length2, length3 = len(s1), len(s2), len(s3)
		if length1 + length2 != length3:
			return False
		dp = [False for _ in range(length2 + 1)]
		dp[0] = True
		for i in range(length1 + 1):
			for j in range(length2 + 1):
				p = i + j - 1
				if i > 0:
					dp[j] = dp[j] and s1[i - 1] == s3[p]
				if j > 0:
					dp[j] = dp[j] or dp[j - 1] and s2[j - 1] == s3[p]
		return dp[length2]
