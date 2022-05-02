class GoUpstairs:
    def countWays(self, n):
        f0, f1, ans = 0, 1, 0
        for _ in range(n):
            f0 = f1
            f1 = ans
            ans = f0 + f1
        return ans % 1000000007
