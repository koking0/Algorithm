#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/H 9:53
# @File     : 面试题 16.11. 跳水板.py
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
	def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
		if k == 0:
			return []
		if shorter == longer:
			return [k * shorter]
		else:
			return list(range(shorter * k, longer * k + 1, longer - shorter))
