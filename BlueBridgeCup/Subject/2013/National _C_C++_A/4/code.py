#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/25 9:57
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


def dfs(x):
	vis[x] = True
	for k in range(len(get[x]) - 1, -1, -1):
		if not vis[get[x][k]] and dfs(get[x][k]):
			vis[x] = False
			return False
	vis[x] = False
	return True


if __name__ == '__main__':
	nums1 = list(map(int, input().split()))
	nums2 = list(map(int, input().split()))
	length1, length2, get, vis = len(nums1), len(nums2), [[] for _ in range(200)], [False] * 200
	for i in range(length1):
		for j in range(i):
			if nums1[i] % nums1[j] == 0 or nums1[j] % nums1[i] == 0:
				get[i].append(j)
				get[j].append(i)
	for i in range(length2):
		for j in range(length1):
			if nums2[i] == nums1[j] and dfs(j):
				print(nums1[j])
				break
		else:
			continue
		break
	else:
		print(-1)
