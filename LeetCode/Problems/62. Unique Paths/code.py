class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n] + [[1] + [0] * (n - 1)]
        print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i % 2][j] = dp[abs(i % 2 - 1)][j] + dp[i % 2][j - 1]
                print(dp)
        return dp[abs(m % 2 - 1)][n - 1]

    def uniquePaths_DP(self, m: int, n: int) -> int:
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]
        
    def uniquePaths_DFS(self, m: int, n: int) -> int:
        def dfs(x: int, y: int):
            # print(f"x = {x}, y = {y}")
            if x == m - 1 and y == n - 1:
                return 1
            if x > m - 1 or y > n - 1:
                return 0
            return dfs(x + 1, y) + dfs(x, y + 1)
        
        return dfs(0, 0)


if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(m=3, n=7))
