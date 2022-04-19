if __name__ == '__main__':
	n = int(input())
	dp = [[0] * (n + 1) for _ in range(n + 1)]
	for i in range(n):
		for j, val in enumerate(map(int, input().split())):
			dp[i][j] = val
	
	# 状态转移，dp[i][j] 表示在第 i 行 j 列的格子能够拿到的最多金币数，dp[i][j] = grid[i][j] + max(dp[i][j + 1], dp[i + 1][j])
	for i in range(n - 1, -1, -1):
		for j in range(n - 1, -1, -1):
			dp[i][j] = dp[i][j] + max(dp[i][j + 1], dp[i + 1][j])
	
	print(dp[0][0])
