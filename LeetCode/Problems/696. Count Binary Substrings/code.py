#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/H/10 7:38
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
	def countBinarySubstrings(self, s: str) -> int:
		ans, cur, last, length = 0, 0, 0, len(s)
		while cur < length:
			c, count = s[cur], 0
			while cur < length and s[cur] == c:
				cur += 1
				count += 1
			ans += min(count, last)
			last = count
		return ans
