#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/5/30 12:38
# @File     : 84. Largest Rectangle in Histogram.py
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
	def largestRectangleArea_Violence_Width(self, heights: List[int]) -> int:
		ans, length = 0, len(heights)
		for i in range(length):
			minHeight = max(heights)
			for j in range(i, length):
				minHeight = min(minHeight, heights[j])
				ans = max((j - i + 1) * minHeight, ans)
		return ans

	def largestRectangleArea_Violence_Height(self, heights: List[int]) -> int:
		ans, length = 0, len(heights)
		for middle in range(length):
			height = heights[middle]
			left, right = middle, middle
			while left - 1 > -1 and heights[left - 1] >= height:
				left -= 1
			while right + 1 < length and heights[right + 1] >= height:
				right += 1
			ans = max(ans, (right - left + 1) * height)
		return ans

	def largestRectangleArea_MonotoneStack(self, heights: List[int]) -> int:
		length = len(heights)
		left, right = [0] * length, [0] * length

		monotoneStack = list()
		for i in range(length):
			while monotoneStack and heights[monotoneStack[-1]] >= heights[i]:
				monotoneStack.pop()
			left[i] = monotoneStack[-1] if monotoneStack else -1
			monotoneStack.append(i)

		monotoneStack = list()
		for i in range(length - 1, -1, -1):
			while monotoneStack and heights[monotoneStack[-1]] >= heights[i]:
				monotoneStack.pop()
			right[i] = monotoneStack[-1] if monotoneStack else length
			monotoneStack.append(i)
		ans = max((right[i] - left[i] - 1) * heights[i] for i in range(length)) if length > 0 else 0
		return ans
