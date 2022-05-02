from typing import List


class Solution:
	def hIndex(self, citations: List[int]) -> int:
		citations.sort(reverse=True)
		for i, v in enumerate(citations):
			if i + 1 > v:
				return i
		return len(citations)
