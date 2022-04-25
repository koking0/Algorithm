from functools import cmp_to_key
from typing import List


class Solution:
	def largestNumber(self, nums: List[int]) -> str:
		nums.sort(key=cmp_to_key(lambda x, y: int(str(y) + str(x)) - int(str(x) + str(y))))
		return str(int(''.join([str(num) for num in nums])))
