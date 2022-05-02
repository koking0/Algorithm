# -*- coding: utf-8 -*-
# @Time        : 2022/2/22 8:48
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
from itertools import permutations


def check(m):
	def dfs(x, y):
		m[x][y] = 0
		for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
			nx, ny = x + dx, y + dy
			if -1 < nx < len(m) and -1 < ny < len(m[0]) and m[nx][ny] == 1:
				dfs(nx, ny)

	cnt = 0
	for r in range(3):
		for c in range(4):
			if m[r][c] == 1:
				dfs(r, c)
				cnt += 1
	return cnt == 1


if __name__ == '__main__':
	ans = set()
	state = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
	matrix = [[0] * 4 for _ in range(3)]
	for ste in permutations(state):
		# 将一维状态向量映射为二维矩阵
		for i in range(3):
			for j in range(4):
				matrix[i][j] = ste[i * 4 + j]

		string = ''.join([''.join(map(str, row)) for row in matrix])
		if check(deepcopy(matrix)) and string not in ans:   # 连通块检查
			print(string)
			ans.add(string)
	print(len(ans))
