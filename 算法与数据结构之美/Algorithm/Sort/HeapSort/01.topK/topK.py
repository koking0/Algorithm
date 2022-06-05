import random


def heapInsert(array: list, index: int):
	while array[int((index - 1) / 2)] > array[index]:
		array[int((index - 1) / 2)], array[index] = array[index], array[int((index - 1) / 2)]
		index = int((index - 1) / 2)


def found(heap: list, k: int):
	for index in range(k):
		heapInsert(heap, index)


def topK(array, k):
	size, heap = len(array), array[0:k]
	# 1.建立一个小根堆
	found(heap, k)
	# B.往小根堆中插入数据
	for index in range(k, size):
		if array[index] > heap[0]:
			heap[0] = array[index]
			found(heap, k)
	return heap


if __name__ == '__main__':
	arr = [random.randint(0, 100) for _ in range(random.randint(10, 15))]
	arr.sort()
	print(arr)
	print(topK(arr, 5))
