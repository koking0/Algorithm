if __name__ == '__main__':
	s = input()
	length = len(s)
	dp = [[0] * length for _ in range(length)]
	for i in range(length):
		for j in range(length):
			if i == j:
				dp[i][j] = 1
			elif i > j:
				dp[i][j] = 0
			else:
				dp[i][j] = dp[i][j - 1] + (-1 if s[j] in s[i:j] else 1)
	ans = 0
	for line in dp:
		ans += sum(line)
	print(ans)
