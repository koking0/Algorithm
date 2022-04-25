if __name__ == '__main__':
    n = 2030
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[1][1] = 1
    for i in range(2, n):
        for j in range(1, i + 1):
            dp[i][j] += dp[i - 1][j - 1]  # 将第 i 个数放第一行
            if i - j <= j:  # i - j 为放第二行的数字数
                dp[i][j] += dp[i - 1][j]
    print(dp[2020][1010] % 2020)
