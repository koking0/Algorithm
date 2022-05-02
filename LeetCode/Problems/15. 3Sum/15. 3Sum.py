#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/6/12 10:21
# @File     : 15. 3Sum.py
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
	def threeSum_violence(self, nums: List[int]) -> List[List[int]]:
		ans, length = [], len(nums)
		for i in range(length):
			for j in range(i + 1, length):
				if -(nums[i] + nums[j]) in nums[j + 1:]:
					temp = sorted([nums[i], nums[j], -(nums[i] + nums[j])])
					if temp not in ans:
						ans.append(temp)
		return ans

	def threeSum(self, nums: List[int]) -> List[List[int]]:
		nums.sort()
		ans, length = list(), len(nums)

		for first in range(length):
			# 需要和上一次枚举的数不相同
			if first > 0 and nums[first] == nums[first - 1]:
				continue
			target, third = -nums[first], length - 1
			for second in range(first + 1, length):
				if second > first + 1 and nums[second] == nums[second - 1]:
					continue
				while second < third and nums[second] + nums[third] > target:
					third -= 1
				if second == third:
					break
				if nums[second] + nums[third] == target:
					ans.append([nums[first], nums[second], nums[third]])
		return ans


a = Solution()
print(a.threeSum([-1, 0, 1, 2, -1, -4]))
