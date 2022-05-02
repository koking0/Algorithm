#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/H/7 H:14
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
	ans = 0
	for i in range(1, 1200000 + 1):
		if 1200000 % i == 0:
			print(i)
			ans += 1
	print(ans)
