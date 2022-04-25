#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/28 7:43
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
	t, n = 0, list(map(int, input().split()))
	length = len(n)
	sub = [0] * length
	for k in range(0, length, 2):
		if k > 1:
			sub[k - 2] = n[k - 1] - n[k - 2] - 1
			if k % 2 == 0:
				t ^= sub[k - 2]
	if not t:
		print(-1)
	else:
		for i in range(length - 1):
			for j in range(1, n[i + 1] - n[i]):
				sub[i] -= j
				if i:
					sub[i - 1] += j
				t = 0
				for m in range(0, length - 1, 2):
					t ^= sub[m]
				if t == 0:
					print(f'{n[i]} {n[i] + j}')
					break
				sub[i] += j
				if i:
					sub[i - 1] -= j
