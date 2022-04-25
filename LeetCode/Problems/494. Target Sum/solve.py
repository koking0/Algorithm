from typing import List


class Solution:
	def findTargetSumWays(self, nums: List[int], target: int) -> int:
		diff = sum(nums) - target

		if diff < 0 or diff % 2:
			return 0

		n = len(nums)
		neg = diff // 2
		dp = [[0 for _ in range((neg + 1))] for _ in range(n + 1)]
		dp[0][0] = 1

		for i in range(1, n + 1):
			num = nums[i - 1]
			for j in range(neg + 1):
				dp[i][j] = dp[i - 1][j]
				if j > num - 1:
					dp[i][j] += dp[i - 1][j - num]
		return dp[n][neg]


if __name__ == '__main__':
	print(Solution().findTargetSumWays([1, 0], 1))
