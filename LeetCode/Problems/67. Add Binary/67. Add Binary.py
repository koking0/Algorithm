#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/6/23 7:40
# @File     : 67. Add Binary.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


class Solution:
	def addBinary(self, a: str, b: str) -> str:
		return bin(int(a, 2) + int(b, 2)).lstrip('0b') or "0"
