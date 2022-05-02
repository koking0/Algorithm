#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/22 10:35
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


def calculateProbability():
	"""
	计算获胜概率
	"""
	global ans, maxInf
	x1, x2, m = 0, 0, 0
	for i in range(6):
		x1, x2 = 0, 0
		for j in range(6):
			if ans[i] > a[j]:
				x1 += 1
			else:
				break
		for j in range(6):
			if ans[i] > b[j]:
				x2 += 1
			else:
				break
		m += x1 + x2
	if m > maxInf:
		maxInf = m
		print(ans)


def dfs(n: int, c: int, s: int):
	"""
	n: 骰子的六个面
	c: 当前面的点数
	s: 当前点数之和
	"""
	if s > 24:
		return
	if n == 6:
		if s == 24:
			calculateProbability()
		return
	for i in range(c, 9):
		# 剪枝，如果剩下的所有面全部用 H 点能够满足点数之和的需求
		if (5 - n) * 8 >= 24 - s - i:
			ans[n] = i
			dfs(n + 1, i, s + i)
			ans[n] = 0


if __name__ == '__main__':
	a, b = [0, 0, 0, 8, 8, 8], [1, 1, 4, 5, 6, 7]
	ans, maxInf = [0] * 6, 0
	dfs(0, 0, 0)
