#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/H/3 7:33
# @File     : code.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> WeChat    : Alex-Paddle
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


class Solution:
	def addStrings(self, num1: str, num2: str) -> str:
		ans, len1, len2, carry = '', len(num1) - 1, len(num2) - 1, 0
		while len1 >= 0 and len2 >= 0:
			ans += str(((int(num1[len1]) + int(num2[len2]) + carry) % 10))
			carry = (int(num1[len1]) + int(num2[len2]) + carry) // 10
			len1 -= 1
			len2 -= 1
		while len1 >= 0:
			ans += str((int(num1[len1]) + carry) % 10)
			carry = (int(num1[len1]) + carry) // 10
			len1 -= 1
		while len2 >= 0:
			ans += str((int(num2[len2]) + carry) % 10)
			carry = (int(num2[len2]) + carry) // 10
			len2 -= 1
		if carry:
			ans += str(carry)
		return ans[::-1]


a = Solution()
print(a.addStrings('584', '18'))
