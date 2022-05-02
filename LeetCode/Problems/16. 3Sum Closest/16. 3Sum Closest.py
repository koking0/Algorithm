#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/6/24 H:36
# @File     : 16. 3Sum Closest.py
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
	def threeSumClosest(self, nums: List[int], target: int) -> int:
		nums.sort()
		length, best = len(nums), 10 ** 7

		def update(cur):
			"""根据差值的绝对值更新答案"""
			nonlocal best
			if abs(cur - target) < abs(best - target):
				best = cur

		# 枚举a
		for i in range(length):
			# 移动到下一个与这次枚举到的不相同的元素
			if i > 0 and nums[i] == nums[i - 1]:
				continue

			# 双指针枚举b和c
			j, k = i + 1, length - 1
			while j < k:
				s = nums[i] + nums[j] + nums[k]
				if s == target:
					return target
				update(s)

				if s > target:
					# 如果和大于 target，移动 c 对应的指针
					k0 = k - 1
					while j < k0 and nums[k0] == nums[k]:
						k0 -= 1
					k = k0
				else:
					# 如果和小于 target，移动 b 对应的指针
					j0 = j + 1
					while k > j0 and nums[j0] == nums[j]:
						j0 += 1
					j = j0
		return best
