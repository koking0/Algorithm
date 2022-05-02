#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/21 10:36
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
	for i in range(1, 20):
		for j in range(i + 1, 20):
			if (i * j) / (i + j) == 6 and (j - i) <= 8:
				print(f'i = {i}, j = {j}')
