#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/4/18 18:36
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


def randomQuickSort(array: list):
	if len(array) < 2:
		return
	_randomQuickSort(array, 0, len(array) - 1)


def _randomQuickSort(array: list, left: int, right: int):
	if left < right:
		less, more = partition(array, left, right, array[random.randint(left, right)])
		_randomQuickSort(array, left, less)
		_randomQuickSort(array, more, right)


def partition(array: list, left: int, right: int, pivot: int):
	less, more = left - 1, right + 1
	while left < more:
		if array[left] < pivot:
			less += 1
			array[left], array[less] = array[less], array[left]
			left += 1
		elif array[left] > pivot:
			more -= 1
			array[left], array[more] = array[more], array[left]
		else:
			left += 1
	return less, more


def bucketSort(array: list):
	length = len(array)
	if length < 2:
		return
	bucketNumber = 10
	maxNumber, bucket = max(array), [[] for _ in range(bucketNumber)]
	for item in array:
		index = min(item // (maxNumber // bucketNumber), bucketNumber - 1)
		bucket[index].append(item)
		randomQuickSort(bucket[index])
	array.clear()
	for value in bucket:
		array.extend(value)


if __name__ == '__main__':
	flag = True
	for i in range(100):
		list1 = [random.randint(0, 100) for _ in range(random.randint(0, 100))]
		list2 = copy.deepcopy(list1)
		list3 = copy.deepcopy(list1)
		bucketSort(list2)
		list3.sort()
		if list2 != list3:
			flag = False
			print(list1)
			print(list2)
			print(list3)
			break
	print("Nice" if flag else "Fuck")
