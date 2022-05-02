def gcd(a, b):
	return a if b == 0 else gcd(b, a % b)


if __name__ == '__main__':
	n = 21
	m = 1 << n
	graph = [[float("inf")] * n for _ in range(n)]
	for i in range(n):
		for j in range(n):
			if gcd(i + 1, j + 1) == 1:
				graph[i][j] = 1
				graph[j][i] = 1
	
	dp = [[0] * n for _ in range(m)]
	dp[1][0] = 1
	for i in range(1, m):
		for j in range(n):
			if i >> j & 1:
				for k in range(n):
					if i - (1 << j) >> k & 1 and graph[k][j]:
						dp[i][j] += dp[i - (1 << j)][k]
	print(sum(dp[m - 1]) - dp[m - 1][0])
