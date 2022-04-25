class Solution:
	def isScramble(self, s1: str, s2: str) -> bool:
		length1, length2 = len(s1), len(s2)
		if length1 != length2:
			return False
		if sorted(s1) != sorted(s2):
			return False
		if s1 == s2:
			return True

		for i in range(1, length1):
			if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or \
				self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
				return True
		return False
