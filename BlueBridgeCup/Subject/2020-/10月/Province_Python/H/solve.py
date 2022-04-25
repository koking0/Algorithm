if __name__ == '__main__':
	n, dp = int(input()), list()
	for i in range(n):
		dp.append(list(map(int, input().split())))
	for i in range(1, n):
		for j in range(i + 1):
			if j == 0:
				dp[i][j] += dp[i - 1][j]
			elif i == j:
				dp[i][j] += dp[i - 1][j - 1]
			else:
				dp[i][j] += max(dp[i - 1][j], dp[i - 1][j - 1])
	print(dp[n - 1][n // 2] if n % 2 else max(dp[n - 1][n // 2 - 1], dp[n - 1][n // 2]))
