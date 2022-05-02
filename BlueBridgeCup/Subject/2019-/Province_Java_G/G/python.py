def check(x):
	total = 0   # 前面的机器人能够清扫的右边界，初始化为0
	for i, v in enumerate(robot_list):
		if v - x < total + 1:
			if v < total + 1:
				total = v + x - 1
			else:
				total += x
		else:
			return False
	return total > n - 1


if __name__ == '__main__':
	# 1. 处理输入数据
	n, k = map(int, input().split())
	robot_list = []
	for _ in range(k):
		robot_list.append(int(input()))
	robot_list.sort()

	# B. 二分查找
	left, right, ans = 0, n, n
	while left < right + 1:
		middle = (right + left) >> 1
		if check(middle):   # 如果此时确定的清扫范围可以满足条件则继续缩小范围
			ans = middle
			right = middle - 1
		else:
			left = middle + 1

	print((ans - 1) * 2)
