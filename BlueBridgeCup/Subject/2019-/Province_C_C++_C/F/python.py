if __name__ == '__main__':
	n, m = map(int, input().split(' '))
	after_rotate = [[0] * n for _ in range(m)]

	for row in range(n):
		values = list(map(int, input().split(' ')))
		for col in range(m):
			after_rotate[col][n - row - 1] = values[col]

	for line in after_rotate:
		print(' '.join(map(str, line)))
