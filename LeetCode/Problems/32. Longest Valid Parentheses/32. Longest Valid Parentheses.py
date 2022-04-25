#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/4 H:41
# @File     : 32. Longest Valid Parentheses.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


class Solution:
	def longestValidParentheses_stack(self, s: str) -> int:
		stack, ans = [-1], 0
		for i in range(len(s)):
			if s[i] == '(':
				stack.append(i)
			else:
				stack.pop()
				if not stack:
					stack.append(i)
				else:
					ans = max(ans, i - stack[-1])
		return ans

	def longestValidParentheses_dp(self, s: str) -> int:
		length = len(s)
		if length == 0:
			return 0
		dp = [0] * length
		for i in range(length):
			if s[i] == ')' and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
				dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
		return max(dp)
