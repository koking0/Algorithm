from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first, second = 0, 0
        for i in range(2, len(cost) + 1):
            val = min(second + cost[i - 1], first + cost[i - 2])
            first, second = second, val
        return second


if __name__ == '__main__':
    solution = Solution()
    print(solution.minCostClimbingStairs(cost=[10, 15, 20]))
