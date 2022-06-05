#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/4/18 12:26
# @File     : BubbleSortCode.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import copy
import random


def countSort(array: list):
	count = [0 for _ in range(max(array) + 1)]
	for value in array:
		count[value] += 1
	array.clear()
	for index, values in enumerate(count):
		for _ in range(values):
			array.append(index)


if __name__ == "__main__":
	flag = True
	for i in range(100):
		list1 = [random.randint(0, 100) for _ in range(random.randint(0, 100))]
		list2 = copy.deepcopy(list1)
		list3 = copy.deepcopy(list1)
		countSort(list2)
		list3.sort()
		if list2 != list3:
			flag = False
			print(list1)
			print(list2)
			print(list3)
			break
	print("Nice" if flag else "Fuck")
