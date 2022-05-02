#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/5/26 H:13
# @File     : 287. Find the Duplicate Number.py
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
	def findDuplicate(self, nums: List[int]) -> int:
		ans, num = None, {}
		for key, value in enumerate(nums):
			if value in num:
				ans = value
			else:
				num[value] = key
		return ans
