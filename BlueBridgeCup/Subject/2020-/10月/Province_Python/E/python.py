def bubbleSortCnt(arr: list) -> int:
	cnt = 0
	for i in range(len(arr) - 1, -1, -1):
		for j in range(i):
			if arr[j] > arr[j + 1]:
				cnt += 1
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
	return cnt


if __name__ == '__main__':
	print(bubbleSortCnt(list("onmlkjihgfedcba")))
	print(bubbleSortCnt(list("jonmlkihgfedcba")))
