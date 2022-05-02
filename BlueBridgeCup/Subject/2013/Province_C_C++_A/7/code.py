#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/H/3 H:27
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
	N, nums, m, n = int(input()), [], 0, 0
	for _ in range(N):
		temp = list(map(int, input().rstrip().split(' ')))
		for item in temp:
			if item in nums:
				n = item
			else:
				nums.append(item)
	nums.sort()
	for i in range(len(nums) - 1):
		if nums[i + 1] != nums[i] + 1:
			m = nums[i] + 1
	print(m, n)
