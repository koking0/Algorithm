#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/6/11 H:54
# @File     : 739. Daily Temperatures.py
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
	def dailyTemperatures_MonotonousStack(self, T: List[int]) -> List[int]:
		length = len(T)
		ans, stack = [0] * length, []
		for index in range(length):
			temperature = T[index]
			while stack and temperature > T[stack[-1]]:
				prevIndex = stack.pop()
				ans[prevIndex] = index - prevIndex
			stack.append(index)
		return ans

	def dailyTemperatures_Violence(self, T: List[int]) -> List[int]:
		ans = []
		for i in range(len(T)):
			for j in range(i + 1, len(T)):
				if T[j] > T[i]:
					ans.append(j - i)
					break
			else:
				ans.append(0)
		return ans


a = Solution()
print(a.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
