#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/4/20 10:04
# @File     : code.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


def findMazePath(startX, startY, endX, endY):
	# 用于记录路径
	pathStack = [(startX, startY)]
	while pathStack:
		current = pathStack[-1]
		# 如果当前节点就是终点
		if current[0] == endX and current[1] == endY:
			for path in pathStack:
				print(path, end=" -> ")
			print("bingo!")
			return True

		directions = [
			lambda x, y: (x + 1, y),
			lambda x, y: (x - 1, y),
			lambda x, y: (x, y + 1),
			lambda x, y: (x, y - 1),
		]
		for direction in directions:
			nextStep = direction(current[0], current[1])
			# 如果下一个节点可以走
			if maze[nextStep[0]][nextStep[1]] == 0:
				# 1.添加到路径中
				pathStack.append(nextStep)
				# B.标记为已走过
				maze[nextStep[0]][nextStep[1]] = 2
				break
		else:
			# 如果for循环正常执行完，说明无路可走，路径中弹出刚才的路线
			pathStack.pop()
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
