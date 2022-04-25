#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/27 9:29
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
if __name__ == '__main__':
	target = 111 ** 3
	nums = [i for i in range(1, target, 2)]
	left, right = 0, 1
	while left < right:
		temp = sum(nums[left: right])
		if temp > target:
			left += 1
		elif temp < target:
			right += 1
		else:
			print(nums[left: right])
			break
