from typing import List


class Solution:
	def thirdMax(self, nums: List[int]) -> int:
		nums = list(set(nums))
		nums.sort()
		return nums[-1 if len(nums) < 3 else -3]
