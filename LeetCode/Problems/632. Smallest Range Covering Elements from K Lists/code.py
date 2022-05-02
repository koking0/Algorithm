#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/H/1 9:45
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
import heapq
from typing import List


class Solution:
	def smallestRange(self, nums: List[List[int]]) -> List[int]:
		rangeLeft, rangeRight = -10 ** 9, 10 ** 9
		# 初始时，k 个指针都指向下标 0，最大元素即为所有列表的下标 0 位置的元素中的最大值
		maxValue = max(vec[0] for vec in nums)
		priorityQueue = [(vec[0], i, 0) for i, vec in enumerate(nums)]
		heapq.heapify(priorityQueue)

		while True:
			minValue, row, idx = heapq.heappop(priorityQueue)
			if maxValue - minValue < rangeRight - rangeLeft:
				rangeLeft, rangeRight = minValue, maxValue
			if idx == len(nums[row]) - 1:
				break
			maxValue = max(maxValue, nums[row][idx + 1])
			heapq.heappush(priorityQueue, (nums[row][idx + 1], row, idx + 1))

		return [rangeLeft, rangeRight]
