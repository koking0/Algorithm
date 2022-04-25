#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/6/29 H:56
# @File     : 215. Kth Largest Element in an Array.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import random
from typing import List


class Solution:
	def findKthLargest_QuickSelection(self, nums: List[int], k: int) -> int:
		def quickSelect(a: List[int], l: int, r: int, k: int):
			q = randomPartition(a, l, r)
			return a[q] if q == k else quickSelect(a, q + 1, r, k) if q < k else quickSelect(a, l, q - 1, k)

		def partition(a: List[int], l: int, r: int):
			x, i = a[r], l - 1
			for j in range(l, r):
				if a[j] <= x:
					i += 1
					a[i], a[j] = a[j], a[i]
			a[i + 1], a[r] = a[r], a[i + 1]
			return i + 1

		def randomPartition(a: List[int], l: int, r: int):
			i = random.randint(l, r)
			a[i], a[r] = a[r], a[i]
			return partition(a, l, r)

		return quickSelect(nums, 0, len(nums) - 1, len(nums) - k)

	def findKthLargest_MinimumHeap(self, nums: List[int], k: int) -> int:
		def shift(i, k):
			flag = 0
			while (i * 2 + 1) < k and flag == 0:
				t = i
				if nums[i] > nums[2 * i + 1]:
					t = 2 * i + 1
				if (i * 2 + 2) < k and nums[t] > nums[2 * i + 2]:
					t = 2 * i + 2
				if t == i:
					flag = 1
				else:
					nums[i], nums[t] = nums[t], nums[i]
					i = t

		for i in range(k // 2, -1, -1):
			shift(i, k)

		for i in range(k, len(nums)):
			if nums[0] < nums[i]:
				nums[0] = nums[i]
				shift(0, k)
		return nums[0]
