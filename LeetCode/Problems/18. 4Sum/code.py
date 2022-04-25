from typing import List


class Solution:
	def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
		length, ans = len(nums), list()
		for i in range(length - 3):
			for j in range(i + 1, length - 2):
				for k in range(j + 1, length - 1):
					if target - (nums[i] + nums[j] + nums[k]) in nums[k + 1:]:
						tmp = sorted([nums[i], nums[j], nums[k], target - (nums[i] + nums[j] + nums[k])])
						if tmp not in ans:
							ans.append(tmp)
		return ans
