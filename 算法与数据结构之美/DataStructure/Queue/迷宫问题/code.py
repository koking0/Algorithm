#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/4/20 10:16
# @File     : code.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
from collections import deque


def printPath(path):
	current, realPath = path[-1], []
	# 从后向前找到走出迷宫的路径
	while current[2] != -1:
		realPath.append(current[0:2])
		current = path[current[2]]
	realPath.append(current[0:2])
	realPath.reverse()
	# 打印走出迷宫路径
	for path in realPath:
		print(path, end=" -> ")
	print("bingo!")


def findMazePath(startX, startY, endX, endY):
	queue, path = deque(), []
	queue.append((startX, startY, -1))
	while queue:
		# 取出当前所在位置
		current = queue.popleft()
		path.append(current)
		# 如果当前节点是终点
		if current[0] == endX and current[1] == endY:
			printPath(path)
			return True

		directions = [
			lambda x, y: (x + 1, y),
			lambda x, y: (x - 1, y),
			lambda x, y: (x, y + 1),
			lambda x, y: (x, y - 1),
		]
		# 遍历四个方位的节点
		for direction in directions:
			nextStep = direction(current[0], current[1])
			# 如果下一个节点可以走
			if maze[nextStep[0]][nextStep[1]] == 0:
				# 1.记录路径和父节点
				queue.append((nextStep[0], nextStep[1], len(path) - 1))
				# B.标记为已走过
				maze[nextStep[0]][nextStep[1]] = 2
	else:
		print('NO PATH TO THROUGH MAZE')
		return False


if __name__ == '__main__':
	maze = [
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
		[1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
		[1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
		[1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
		[1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
		[1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
		[1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
	]
	findMazePath(startX=1, startY=1, endX=8, endY=8)
