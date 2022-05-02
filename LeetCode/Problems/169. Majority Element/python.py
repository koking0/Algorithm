from typing import List
from collections import Counter


class Solution:
	def majorityElement(self, nums: List[int]) -> int:
		counter = Counter(nums)
		return counter.most_common(1)[0][0]
