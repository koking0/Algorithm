#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/5/20 21:45
# @File     : 1371. Find the Longest Substring Containing Vowels in Even Counts.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


class Solution:
	def findTheLongestSubstring(self, s: str) -> int:
		mapper = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
		seen = {0: -1}
		res = cur = 0

		for i in range(len(s)):
			if s[i] in mapper:
				cur ^= mapper.get(s[i])
			if cur in seen:
				res = max(res, i - seen.get(cur))
			else:
				seen[cur] = i
		return res
