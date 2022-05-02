if __name__ == '__main__':
	point_list = []
	n = int(input())
	for _ in range(n):
		point_list.append(tuple(map(int, input().split())))

	max_x = 0
	point_list.sort(key=lambda x: x[1])
	for i in range(n - 1, -1, -1):
		if point_list[i][0] > max_x:
			print(f"{point_list[i][0]} {point_list[i][1]}")
			max_x = point_list[i][0]
