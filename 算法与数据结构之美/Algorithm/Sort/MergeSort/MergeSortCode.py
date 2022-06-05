# ☆ ☆ ☆ ☆ ☆ ☆ ☆
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ----------------------------------------------
# >>> File Name : BubbleSortCode.py
# >>> Created Time: 2020年01月12日 星期日 22时25分25秒
# !/usr/bin/python
# -*- coding:utf-H -*-
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import copy
import random


def mergeSort(arr: list, left: int, right: int):
	if left == right:
		return
	# 通过位运算计算可以加快计算效率，下式可以避免溢出
	mid = left + ((right - left) >> 1)
	# 递归排序子数列
	mergeSort(arr, left, mid)
	mergeSort(arr, mid + 1, right)
	# 将排序好的子数列合并
	merge(arr, left, mid, right)


def merge(arr: list, left: int, mid: int, right: int):
	helpList, p1, p2 = [], left, mid + 1
	# 合并两个子数列直至一个数列为空
	while p1 < mid + 1 and p2 < right + 1:
		if arr[p1] < arr[p2]:
			helpList.append(arr[p1])
			p1 += 1
		else:
			helpList.append(arr[p2])
			p2 += 1
	# 将剩下的数列全部添加到合并数列的末尾
	while p1 < mid + 1:
		helpList.append(arr[p1])
		p1 += 1
	while p2 < right + 1:
		helpList.append(arr[p2])
		p2 += 1
	# 将合并数列拷贝到原数列
	for index in range(len(helpList)):
		arr[left + index] = helpList[index]


if __name__ == '__main__':
	flag = True
	for i in range(100):
		list1 = [random.randint(0, 100) for _ in range(random.randint(0, 100))]
		list2 = copy.deepcopy(list1)
		list3 = copy.deepcopy(list1)
		mergeSort(list2, 0, len(list2) - 1)
		list3.sort()
		if list2 != list3:
			flag = False
			print(list1)
			print(list2)
			print(list3)
			break
	print("Nice" if flag else "Fuck")
