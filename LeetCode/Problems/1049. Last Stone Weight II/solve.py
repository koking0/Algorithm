from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        n, m = len(stones), total // 2
        dp = [False] * (m + 1)
        dp[0] = True

        for weight in stones:
            for j in range(m, weight - 1, -1):
                dp[j] |= dp[j - weight]

        ans = 0
        for j in range(m, -1, -1):
            if dp[j]:
                ans = total - 2 * j
                break
        return ans
