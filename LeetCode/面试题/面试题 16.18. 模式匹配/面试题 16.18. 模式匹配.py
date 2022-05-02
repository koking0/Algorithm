#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/6/22 H:21
# @File     : 面试题 16.18. 模式匹配.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


class Solution:
	def patternMatching(self, pattern: str, value: str) -> bool:
		countA = sum(1 for c in pattern if c == 'a')
		countB = len(pattern) - countA
		if countA < countB:
			countA, countB = countB, countA
			pattern = "".join('a' if c == 'b' else 'b' for c in pattern)

		if not value:
			return countB == 0
		if not pattern:
			return False

		for lenA in range(len(value) // countA + 1):
			rest = len(value) - countA * lenA
			if (countB == 0 and rest == 0) or (countB != 0 and rest % countB == 0):
				lenB = 0 if countB == 0 else rest // countB
				pos, correct = 0, True
				valueA, valueB = None, None
				for c in pattern:
					if c == 'a':
						sub = value[pos: pos + lenA]
						if not valueA:
							valueA = sub
						elif valueA != sub:
							correct = False
							break
						pos += lenA
					else:
						sub = value[pos: pos + lenB]
						if not valueB:
							valueB = sub
						elif valueB != sub:
							correct = False
							break
						pos += lenB
				if correct and valueA != valueB:
					return True
		return False
