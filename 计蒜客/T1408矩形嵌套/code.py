#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/6 12:36
# @File     : code.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


def inputMatrix(n):
	rectangles = []
	for _ in range(n):
		ab = list(map(int, input().split(' ')))
		rectangles.append(ab)
	return rectangles


def createGraph(m, n):
	return [[1 if (m[i][0] > m[j][0] and m[i][1] > m[j][1]) or (m[i][0] > m[j][1] and m[i][1] > m[j][0]) else 0
	         for j in range(n)] for i in range(n)]


def dp(i):
	if vis[i] > 0:
		return vis[i]
	vis[i] = 1
	for j in range(n):
		if graph[i][j]:
			vis[i] = vis[i] if vis[i] > dp(j) + 1 else dp(j) + 1
	return vis[i]


if __name__ == '__main__':
	N = int(input())
	for _ in range(N):
		n = int(input())
		matrix = inputMatrix(n)
		graph = createGraph(matrix, n)
		ans, vis = 1, [0] * n
		for i in range(n):
			ans = max(dp(i), ans)
		print(ans)
