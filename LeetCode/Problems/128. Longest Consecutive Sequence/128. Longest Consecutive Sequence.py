#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/6/6 7:44
# @File     : 128. Longest Consecutive Sequence.py
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
	def longestConsecutive(self, nums: List[int]) -> int:
		if not nums:
			return 0

		nums.sort()
		ans, temp = 0, 0
		for index in range(1, len(nums)):
			if nums[index] - nums[index - 1] == 1:
				temp += 1
			elif nums[index] - nums[index - 1] == 0:
				continue
			else:
				ans = max(ans, temp)
				temp = 0
		ans = max(ans, temp)
		return ans + 1


a = Solution()
print(a.longestConsecutive([1,2,0,1]))
