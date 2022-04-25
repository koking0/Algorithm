# -*- coding: utf-8 -*-
# @Time        : 2022/2/21 8:38
# @File        : python.py
# @Description : None
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> Mail      : liu_zhao_feng_alex@163.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
from collections import deque


def bfs(x, y, step):
	queue = deque()
	queue.append((x, y, step))
	visit[x][y] = True

	while queue:
		front = queue.popleft()
		x, y, step = front

		if matrix[x][y] == 'B':
			return step

		for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
			nx, ny = x + dx, y + dy
			if -1 < nx < n and -1 < ny < n and not visit[nx][ny] and matrix[x][y] != matrix[nx][ny]:
				visit[nx][ny] = True
				queue.append((nx, ny, step + 1))

	return -1


if __name__ == '__main__':
	n = int(input())
	visit = [[False] * n for _ in range(n)]
	matrix = [[None] * n for _ in range(n)]

	ai, aj = 0, 0
	for i in range(n):
		for j, v in enumerate(input().split()):
			matrix[i][j] = v

			if v == 'A':
				ai, aj = i, j

	print(bfs(ai, aj, 0))
