#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/1/12 下午5:43
# @Author   : alex
# @File     : BubbleSortCode.py
# @Project  : Algorithm
# @Software : PyCharm
import copy
import random


def bubbleSort(arr: list):
	length = len(arr)
	for trip in range(length):
		for index in range(length - trip - 1):
			# 相邻的两个元素，如果顺序错误，就交换两个的位置
			if arr[index] > arr[index + 1]:
				arr[index], arr[index + 1] = arr[index + 1], arr[index]


def bubbleSortV1(arr: list):
	length = len(arr)
	for trip in range(length):
		# 交换标志
		exChange = False
		for index in range(length - trip - 1):
			# 相邻的两个元素，如果顺序错误，就交换两个的位置
			if arr[index] > arr[index + 1]:
				# 如果有交换发生， 标记为 True
				exChange = True
				arr[index], arr[index + 1] = arr[index + 1], arr[index]
		# 如果没有交换发生，说明数列已经有序了
		if not exChange:
			break


if __name__ == '__main__':
	flag = True
	for i in range(100):
		list1 = [random.randint(0, 100) for _ in range(random.randint(0, 100))]
		list2 = copy.deepcopy(list1)
		list3 = copy.deepcopy(list1)
		bubbleSortV1(list2)
		list3.sort()
		if list2 != list3:
			flag = False
			print(list1)
			print(list2)
			print(list3)
			break
	print("Nice" if flag else "Fuck")
