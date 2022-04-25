class Bonus:
    def getMost(self, board):
        dp = [[0] * 6 for _ in range(6)]
        dp[0][0] = board[0][0]
        for i in range(1, 6):
            dp[0][i] = board[0][i] + dp[0][i - 1]
            dp[i][0] = board[i][0] + dp[i - 1][0]
        for i in range(1, 6):
            for j in range(1, 6):
                dp[i][j] = board[i][j] + max(dp[i - 1][j], dp[i][j - 1])
        return dp[5][5]
