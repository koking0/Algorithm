from typing import List


class Solution:
    def minCount(self, coins: List[int]) -> int:
        ans = 0
        for coin in coins:
            if coin & 1:
                ans += 1 + coin // 2
            else:
                ans += coin // 2
        return ans
