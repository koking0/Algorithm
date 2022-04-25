#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/6/24 13:29
# @File     : code.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import random


def binarySearch(array: list, target: int):
	n = len(array)
	if 0 == n:
		return False
	mid = n // 2
	if array[mid] == target:
		return True
	elif target < array[mid]:
		return binarySearch(array[:mid], target)
	else:
		return binarySearch(array[mid + 1:], target)


if __name__ == '__main__':
	target = random.randint(0, 100)
	test = [random.randint(0, 100) for _ in range(random.randint(0, 10))]
	print(f'test = {test}')
	print(f'target = {target}')
	print(f'binary search = {binarySearch(test, target)}')
