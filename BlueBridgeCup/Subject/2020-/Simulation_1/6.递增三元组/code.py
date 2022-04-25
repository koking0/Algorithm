#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/H/11 H:48
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
	ans, n = set(), int(input())
	a = list(map(int, input().split(' ')))
	for i in range(len(a)):
		for j in range(i + 1, len(a)):
			for k in range(j + 1, len(a)):
				if a[i] < a[j] < a[k]:
					ans.add(j)
	print(len(ans))
