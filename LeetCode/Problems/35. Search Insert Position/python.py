from typing import List


class Solution:
	def searchInsert(self, nums: List[int], target: int) -> int:
		ans, left, right = len(nums), 0, len(nums) - 1
		while left <= right:
			middle = ((right - left) >> 1) + left
			if target <= nums[middle]:
				right = middle - 1
				ans = middle
			else:
				left = middle + 1
		return ans


if __name__ == '__main__':
	print(Solution().searchInsert(nums=[1, 3, 5, 6], target=7))
