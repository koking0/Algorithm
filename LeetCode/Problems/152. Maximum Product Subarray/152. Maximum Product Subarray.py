#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/5/18 21:22
# @File     : 152. Maximum Product Subarray.py
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
	def maxProduct(self, nums: List[int]) -> int:
		maxF, minF, ans = nums[0], nums[0], nums[0]
		for i in range(1, len(nums)):
			mx, mn = maxF, minF
			maxF = max(mx * nums[i], max(mn * nums[i], nums[i]))
			minF = min(mn * nums[i], min(mx * nums[i], nums[i]))
			ans = max(ans, maxF)
		return ans


a = Solution()
print(a.maxProduct(nums=[-2, 3, -4]))
