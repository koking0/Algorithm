#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/4/22 21:24
# @File     : KMP.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
# KMP算法
# 首先计算nextList数组，即需要怎么去移位
# 接着就是用暴力解法求解即可
# nextList是用循环来实现的


def genNext(str2):
	k, n, j = -1, len(str2), 0
	nextList = [0 for _ in range(n)]
	nextList[0] = -1  # next数组初始值为-1
	while j < n - 1:
		if k == -1 or str2[k] == str2[j]:
			k += 1
			j += 1
			nextList[j] = k  # 如果相等 则next[j+1] = k
		else:
			k = nextList[k]  # 如果不等，则将next[k]的值给k
	return nextList


def match(str1, str2, nextList):
	ans, i, j = -1, 0, 0
	while i < len(str1):
		if str1[i] == str2[j] or j == -1:
			i += 1
			j += 1
		else:
			j = nextList[j]
		if j == len(str2):
			ans = i - len(str2)
			break
	return ans


if __name__ == '__main__':
	s1 = 'ababaacc'
	s2 = 'abaa'
	next_list = genNext(s2)
	print(next_list)
	print(match(s1, s2, next_list))
