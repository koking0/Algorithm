from typing import List


class Solution:
	def maxAliveYear(self, birth: List[int], death: List[int]) -> int:
		nums = [0] * 101
		for i, v in enumerate(birth):
			for j in range(v, death[i] + 1):
				nums[j - 1900] += 1
		return nums.index(max(nums)) + 1900
