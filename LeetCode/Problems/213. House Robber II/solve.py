from typing import List


class Solution:
	def rob(self, nums: List[int]) -> int:
		def rob_range(s: int, e: int):
			first, second = nums[s], max(nums[s], nums[s + 1])
			for i in range(s + 2, e + 1):
				first, second = second, max(first + nums[i], second)
			return second

		length = len(nums)
		if length == 1:
			return nums[0]
		elif length == 2:
			return max(nums[0], nums[1])
		else:
			return max(rob_range(0, length - 2), rob_range(1, length - 1))


if __name__ == '__main__':
	print(Solution().rob(nums=[2, 3, 2]))
