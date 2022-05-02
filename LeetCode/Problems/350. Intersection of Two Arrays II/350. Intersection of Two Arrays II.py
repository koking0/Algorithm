#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/13 9:15
# @File     : 350. Intersection of Two Arrays II.py
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
	def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
		nums1.sort()
		nums2.sort()
		i, j, length1, length2, ans = 0, 0, len(nums1), len(nums2), []
		while i < length1 and j < length2:
			if nums1[i] == nums2[j]:
				ans.append(nums1[i])
				i += 1
				j += 1
			elif nums1[i] < nums2[j]:
				i += 1
			else:
				j += 1
		return ans
