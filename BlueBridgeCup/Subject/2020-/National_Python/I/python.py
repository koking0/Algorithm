def distance(i, j):
	x, y = xy_list[i][0] - xy_list[j][0], xy_list[i][1] - xy_list[j][1]
	return (x ** 2 + y ** 2) ** 0.5


if __name__ == '__main__':
	n, d = map(int, input().split())
	xy_list = []
	for _ in range(n):
		xy_list.append(list(map(int, input().split())))
	
	w = [[0] * n for _ in range(n)]
	f = [[1e9] * n for _ in range(n >> 1)]
	for i in range(n):
		for j in range(i + 1, n):
			w[i][j] = w[j][i] = distance(i, j)
			if w[i][j] > d:
				w[i][j] = w[j][i] = 1e9
	
	for k in range(0, n):
		for i in range(0, n):
			for j in range(0, n):
				w[i][j] = min(w[i][j], w[i][k] + w[k][j])
	print(f"w = {w}")
	
	f[1][0] = 0
	for i in range(n >> 1):
		for j in range(n):
			if i >> j & 1:
				for k in range(n):
					if (i - (1 << j)) >> k & 1:
						f[i][j] = min(f[i][j], f[i - (j >> 1)][k] + w[k][j])
	
	print(f"f = {f}")
	ans = 1e9
	for i in range(1, n):
		ans = min(ans, f[(n >> 1) - 1][i] + w[i][0])
	print(f"{ans:.2f}")
