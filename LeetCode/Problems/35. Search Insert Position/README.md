## Ideas

题目中给的提示已经很清楚了，要求时间复杂度是O(log n)，这不是指着鼻子跟我说：给老子用二分查找嘛！

## Code

### Python

```python
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
```