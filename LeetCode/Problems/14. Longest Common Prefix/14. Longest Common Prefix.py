#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/6/15 H:19
# @File     : 14. Longest Common Prefix.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
from typing import List


class Solution:
	def longestCommonPrefix_transverseScan(self, strs: List[str]) -> str:
		def lcp(str1, str2):
			index, length = 0, min(len(str1), len(str2))
			while index < length and str1[index] == str2[index]:
				index += 1
			return str1[: index]

		if not strs:
			return ""

		prefix = strs[0]
		for i in range(1, len(strs)):
			prefix = lcp(prefix, strs[i])
			if not prefix:
				break
		return prefix

	def longestCommonPrefix_longitudinalScan(self, strs: List[str]) -> str:
		if not strs:
			return ""

		for i in range(len(strs[0])):
			char = strs[0][i]
			for j in range(1, len(strs)):
				if i == len(strs[j]) or strs[j][i] != char:
					return strs[0][:i]
		return strs[0]

	def longestCommonPrefix_divideAndConquer(self, strs: List[str]) -> str:
		def lcp(left, right):
			if left == right:
				return strs[left]

			middle = (left + right) // 2
			leftLcp, rightLcp = lcp(left, middle), lcp(middle + 1, right)
			minLength = min(len(leftLcp), len(rightLcp))
			for i in range(minLength):
				if leftLcp[i] != rightLcp[i]:
					return leftLcp[:i]
			return leftLcp[: minLength]

		return "" if not strs else lcp(0, len(strs) - 1)

	def longestCommonPrefix_python(self, strs: List[str]) -> str:
		for index, value in enumerate((*(len(set(item)) for item in zip(*strs)), 2)):
			if value > 1:
				return (*strs, "")[0][: index]


if __name__ == '__main__':
	strings = ["abc", "abcd", "azcd", "aacc"]
	print(*strings)
	for item in zip(*strings):
		print(len(set(item)))
