#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/6/4 6:58
# @File     : 238. Product of Array Except Self.py
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
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		length, answer = len(nums), [1]
		for i in range(1, length):
			answer.append(nums[i - 1] * answer[i - 1])
		R = 1
		for i in range(length - 1, -1, -1):
			answer[i] = answer[i] * R
			R *= nums[i]
		return answer
