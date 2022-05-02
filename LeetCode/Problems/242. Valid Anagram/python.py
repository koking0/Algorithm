from collections import Counter


class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		counterS = Counter(s)
		counterT = Counter(t)
		return counterS == counterT
