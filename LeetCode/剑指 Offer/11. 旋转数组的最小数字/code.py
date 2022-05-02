#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/22 9:02
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
from typing import List


class Solution:
	def minArray(self, numbers: List[int]) -> int:
		left, right = 0, len(numbers) - 1
		while left < right:
			middle = left + (right - left) // 2
			if numbers[middle] < numbers[right]:
				right = middle
			elif numbers[middle] > numbers[right]:
				left = middle + 1
			else:
				right -= 1
		return numbers[left]
