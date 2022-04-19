if __name__ == '__main__':
    n, m = map(int, input().split())
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if j == 1:
                dp[i][j] = (1 / n) ** (i - 1)
            else:
                dp[i][j] = dp[i - 1][j] * (j / n) + dp[i - 1][j - 1] * ((n - j + 1) / n)
    print(f"{dp[m][n]:.4f}")
