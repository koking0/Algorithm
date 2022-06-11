# -*- coding: utf-8 -*-
# @Author   : Alex
# @Time     : 2022/6/11 8:07
# @File     : python.py
# @Software : PyCharm
# Email     : liu_zhao_feng_alex@163.com
# Blog      : https://alex007.blog.csdn.net/
from collections import Counter
from typing import List


class Solution:
	def findJudge(self, n: int, trust: List[List[int]]) -> int:
		ans, in_degree, out_degree = -1, Counter(), Counter()
		for (start, end) in trust:
			in_degree[end] += 1
			out_degree[start] += 1
		for i in range(1, n + 1):
			if in_degree[i] == n - 1 and out_degree[i] == 0:
				ans = i
		return ans
