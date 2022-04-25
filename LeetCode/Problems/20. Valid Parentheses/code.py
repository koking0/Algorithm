#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/H/14 9:54
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
	def isValid(self, s: str) -> bool:
		if len(s) % 2 != 0:
			return False

		stack = []
		for c in list(s):
			if c in ['(', '[', '{']:
				stack.append(c)
			elif c == ')' and (len(stack) == 0 or stack.pop() != '('):
				return False
			elif c == ']' and (len(stack) == 0 or stack.pop() != '['):
				return False
			elif c == '}' and (len(stack) == 0 or stack.pop() != '{'):
				return False
		return len(stack) == 0
