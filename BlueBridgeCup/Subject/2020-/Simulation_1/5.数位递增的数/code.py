#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/H/10 H:54
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
	ans, n = 0, int(input())
	for i in range(1, n):
		temp = list(map(int, list(str(i))))
		temp.sort()
		if i == int(''.join(list(map(str, temp)))):
			ans += 1
	print(ans)
