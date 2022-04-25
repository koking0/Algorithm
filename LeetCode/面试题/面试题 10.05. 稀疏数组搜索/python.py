from typing import List


class Solution:
	def findString(self, words: List[str], s: str) -> int:
		left, right = 0, len(words) - 1
		while left < right + 1:
			# 过滤空字符串
			while left < right + 1 and not words[left]:
				left += 1
			while left < right + 1 and not words[right]:
				right -= 1
			if left > right:
				return -1

			middle = ((right - left) >> 1) + left
			while middle < right and not words[middle]:
				middle += 1
			if words[middle] == s:
				return middle
			elif words[middle] > s:
				right = middle - 1
			elif words[middle] < s:
				left = middle + 1
		return -1
