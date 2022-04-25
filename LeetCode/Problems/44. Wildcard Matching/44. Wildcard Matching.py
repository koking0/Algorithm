#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/5 9:07
# @File     : 44. Wildcard Matching.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


class Solution:
	def isMatch(self, s: str, p: str) -> bool:
		lengthS, lengthP = len(s), len(p)
		dp = [[False] * (lengthP + 1) for _ in range(lengthS + 1)]
		dp[0][0] = True
		for i in range(1, lengthP + 1):
			if p[i - 1] == '*':
				dp[0][i] = True
			else:
				break
		for i in range(1, lengthS + 1):
			for j in range(1, lengthP + 1):
				if p[j - 1] == '*':
					dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
				elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
					dp[i][j] = dp[i - 1][j - 1]
		return dp[lengthS][lengthP]
