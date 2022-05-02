#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/H/13 H:16
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


class Solution:
	def multiply(self, num1: str, num2: str) -> str:
		if num1 == '0' or num2 == '0':
			return '0'

		len1, len2 = len(num1), len(num2)
		ans = [0 for _ in range(230)]
		for i in range(len1):
			for j in range(len2):
				ans[len1 - i + len2 - j - 1] += int(num1[i]) * int(num2[j])
		for i in range(1, len1 + len2 + 1):
			ans[i + 1] += ans[i] // 10
			ans[i] %= 10
		ans[0] = len1 + len2
		while ans[ans[0]] == 0 and ans[0] > 1:
			ans[0] -= 1
		return ''.join(list(map(str, ans[1: ans[0] + 1][::-1])))


a = Solution()
print(a.multiply('123', '456'))
