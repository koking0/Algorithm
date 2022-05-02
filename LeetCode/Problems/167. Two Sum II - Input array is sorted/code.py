#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/20 H:10
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
	def twoSum(self, numbers: List[int], target: int) -> List[int]:
		left, right = 0, len(numbers) - 1
		while left < right:
			if numbers[left] + numbers[right] > target:
				right -= 1
			elif numbers[left] + numbers[right] < target:
				left += 1
			else:
				return [left + 1, right + 1]
