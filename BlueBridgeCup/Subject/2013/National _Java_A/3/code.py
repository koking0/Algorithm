#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/30 H:39
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
	ans, c, d = 0, 2, 45
	for a in range(22, 46):
		for b in range(a + 1, 10000):
			if a * d + b * d == a * b * c:
				print(f'1/{a} + 1/{b} = {c}/{d}')
				ans += 1
	print(ans)
