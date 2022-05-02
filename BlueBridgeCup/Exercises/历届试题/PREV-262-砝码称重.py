if __name__ == "__main__":
    N = int(input())
    W = list(map(int, input().split()))

    total = sum(W)
    dp = [[0] * (total * 2) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, total + 1):
            # 使用 i - 1 个砝码能够得到的重量，使用 i 个砝码肯定也可以得到
            dp[i][j] = dp[i - 1][j]
            if not dp[i][j]:
                # 当前要判断的砝码称重存在现成的砝码
                if j == W[i - 1]:
                    dp[i][j] = 1
                # 当前要判断的砝码称重与上1轮组合出来的重量放在不同侧，判断是否可以组成j
                if dp[i - 1][j + W[i - 1]]:
                    dp[i][j] = 1
                # 当前要判断的砝码称重与上1轮组合出来的重量放在相同侧，判断是否可以组成j
                if dp[i - 1][abs(j - W[i - 1])]:
                    dp[i][j] = 1

    print(sum(dp[N]))
