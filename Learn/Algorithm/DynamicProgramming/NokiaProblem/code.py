import sys

if __name__ == '__main__':
	floors, phones = 100, 10
	dp = [[0 for _ in range(phones)] for _ in range(floors)]
	for t in range(floors):
		dp[t][0] = t + 1
	for n in range(phones):
		dp[0][n] = 1
	for t in range(1, floors):
		for n in range(1, phones):
			num = sys.maxsize
			for k in range(1, t + 1):
				num = min(num, 1 + max(dp[k - 1][n - 1], dp[t - k - 1][n]))
			dp[t][n] = num
	for t in range(100):
		print(f"Floor = {t + 1}:\t", end="")
		for n in range(10):
			print(dp[t][n], end=" ")
		print()
