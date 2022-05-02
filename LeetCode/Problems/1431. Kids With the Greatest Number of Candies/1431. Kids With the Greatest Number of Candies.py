#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/6/1 9:00
# @File     : 1431. Kids With the Greatest Number of Candies.py
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
	def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
		return [bool(item + extraCandies >= max(candies)) for item in candies]
