#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/26 H:57
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


def dfs(x, pre, step):
	if step == 3:
		global ans
		ans += 1
		return
	for i in range(len(graph[x])):
		if graph[x][i] != pre:
			dfs(graph[x][i], x, step + 1)


if __name__ == '__main__':
	n, m = map(int, input().split())
	ans, graph = 0, [[] for _ in range(10007)]
	for _ in range(m):
		u, v = map(int, input().split())
		graph[u].append(v)
		graph[v].append(u)
	for i in range(1, n + 1):
		dfs(i, 0, 0)
	print(ans)
