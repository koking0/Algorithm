#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/5/23 9:35
# @File     : 76. Minimum Window Substring.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


class Solution:
	def minWindow(self, s: str, t: str) -> str:
		import collections
		n, left, ans, cnt = 0, 0, '', collections.Counter(t)
		for right, ch in enumerate(s):
			if ch not in cnt:
				continue
			# 统计当前字符，判断是否已经达到数量要求
			cnt[ch] -= 1
			if cnt[ch] == 0:
				n += 1
			# 如果当前在left的字符没有必要，可以右移左指针
			while s[left] not in cnt or cnt[s[left]] < 0:
				if s[left] in cnt:
					cnt[s[left]] += 1
				left += 1
			if n == len(cnt):
				if not ans or len(ans) > right - left + 1:
					ans = s[left: right + 1]
		return ans
