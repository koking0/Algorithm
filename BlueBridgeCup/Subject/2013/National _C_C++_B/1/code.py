#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/27 H:50
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
# ABC * ABC = ADEFGB
if __name__ == '__main__':
	for i in range(1, 10):
		for j in range(10):
			for k in range(10):
				if i != j and j != k and i != k:
					num = i * 100 + j * 10 + k
					product = list(map(int, list(str(num * num))))
					if i == product[0] and j == product[-1]:
						print(f'{num} * {num} = {num * num}')
