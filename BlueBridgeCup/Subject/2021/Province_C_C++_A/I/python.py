def process():
	l_cnt, r_cnt, num, add = 0, 0, 0, [0] * n
	for i in range(n):
		if s[i] == '(':
			l_cnt += 1
		else:
			r_cnt += 1
			num += 1
			if l_cnt:
				l_cnt -= 1
				r_cnt -= 1
			add[num] = r_cnt
	
	dp = [[0] * n for _ in range(n)]
	for i in range(add[0], n):
		dp[0][i] = 1
	
	for i in range(1, num):
		for j in range(0, add[i]):
			dp[i][add[i]] = (dp[i][add[i]] + dp[i - 1][j]) % mod
		for j in range(add[i] + 1, n):
			dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % mod
	
	return dp[num][r_cnt]


if __name__ == '__main__':
	s = input()
	n = len(s)
	mod = 1e9 + 7
	
	ans = process()
	for i in range(n):
		s[i] = '(' if s[i] == ')' else ')'
	s = reversed(s)
	ans = (ans * process()) % mod
	print(ans)
	
