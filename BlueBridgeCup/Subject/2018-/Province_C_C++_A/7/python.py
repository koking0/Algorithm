# -*- coding: utf-8 -*-
# @Time        : 2022/2/28 21:04
# @File        : python.py
# @Description : None
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> Mail      : liu_zhao_feng_alex@163.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
from copy import deepcopy


def get(i, j, k) -> int:
	return (i * B + j) * C + k


def check(mid):
	b = deepcopy(bp)
	for i in range(1, mid + 1):
		x1, x2 = op[i][0], op[i][1]
		y1, y2 = op[i][2], op[i][3]
		z1, z2 = op[i][4], op[i][5]
		c = op[i][6]

		b[get(x1, y1, z1)] -= c
		b[get(x1, y1, z2 + 1)] += c
		b[get(x1, y2 + 1, z1)] += c
		b[get(x1, y2 + 1, z2 + 1)] -= c
		b[get(x2 + 1, y1, z1)] += c
		b[get(x2 + 1, y1, z2 + 1)] -= c
		b[get(x2 + 1, y2 + 1, z1)] -= c
		b[get(x2 + 1, y2 + 1, z2 + 1)] += c

	s = [0] * ((A + 1) * (B + 1) * (C + 1))
	for i in range(1, A + 1):
		for j in range(1, B + 1):
			for k in range(1, C + 1):
				s[get(i, j, k)] += b[get(i, j, k)]
				for u in range(1, 8):
					x = i - d[u][0]
					y = j - d[u][1]
					z = k - d[u][2]
					t = d[u][3]
					s[get(i, j, k)] -= s[get(x, y, z)] * t
				if s[get(i, j, k)] < 0:
					return True
	return False


if __name__ == '__main__':
	A, B, C, m = map(int, input().split())

	s = [0] * ((A + 1) * (B + 1) * (C + 1))  # 原数组
	for val in input().split():
		for i in range(1, A + 1):
			for j in range(1, B + 1):
				for k in range(1, C + 1):
					s[get(i, j, k)] = int(val)

	# 计算差分数组
	d = [[0, 0, 0, 1], [0, 0, 1, -1], [0, 1, 0, -1], [0, 1, 1, 1],
	     [1, 0, 0, -1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, -1]]
	bp = [0] * ((A + 1) * (B + 1) * (C + 1))  # 差分数组
	for i in range(1, A + 1):
		for j in range(1, B + 1):
			for k in range(1, C + 1):
				for u in range(8):
					x = i - d[u][0]
					y = j - d[u][1]
					z = k - d[u][2]
					t = d[u][3]
					bp[get(i, j, k)] += s[get(x, y, z)] * t

	# 读入攻击操作
	op = [[0] * 7 for _ in range(m + 1)]
	for i in range(1, m + 1):
		vals = input().split()
		for j in range(7):
			op[i][j] = int(vals[j])

	# 二分查找答案
	left, right = 1, m
	while left < right:
		middle = (left + right) >> 1
		if check(middle):
			right = middle
		else:
			left = middle + 1

	print(right)
