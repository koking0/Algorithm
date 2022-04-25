#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/5/28 9:02
# @File     : 394. Decode String.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


class Solution:
	def decodeString(self, s: str) -> str:
		stack = []
		for index, value in enumerate(s):
			stack.append(value)
			if value == ']':
				for i in range(len(stack) - 2, -1, -1):
					if stack[i] == '[':
						string = stack[i + 1: len(stack) - 1]
						for j in range(i - 1, -1, -1):
							if j == 0 or not stack[j - 1].isdigit():
								num = int(''.join(stack[j:i]))
								stack = stack[:j]
								stack.extend(num * string)
								break
						break
		return ''.join(stack)
