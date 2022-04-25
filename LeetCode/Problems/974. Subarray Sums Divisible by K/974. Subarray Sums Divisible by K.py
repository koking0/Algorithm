#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/5/27 H:27
# @File     : 974. Subarray Sums Divisible by K.py
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
	def subarraysDivByK_violence(self, A: List[int], K: int) -> int:
		ans = 0
		for i in range(len(A)):
			for j in range(i + 1, len(A) + 1):
				if sum(A[i:j]) % K == 0:
					ans += 1
		return ans

	def subarraysDivByK(self, A: List[int], K: int) -> int:
		ans, preSum, modKMap = 0, 0, {0: 1}
		for i in range(len(A)):
			preSum = (preSum + A[i]) % K
			# 因为负数取模还是负数，所以需要加 K
			if preSum < 0:
				preSum += K
			if modKMap.get(preSum, None):
				ans += modKMap[preSum]
				modKMap[preSum] += 1
			else:
				modKMap[preSum] = 1
		return ans


a = Solution()
print(a.subarraysDivByK([4, 5, 0, -2, -3, 1], 5))
