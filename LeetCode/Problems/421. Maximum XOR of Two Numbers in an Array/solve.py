from typing import List


class Trie:
	def __init__(self):
		self.left, self.right = None, None


class Solution:
	def findMaximumXOR(self, nums: List[int]) -> int:
		root = Trie()
		HIGH_BIT = 30

		def add(num: int) -> None:
			cur = root
			for k in range(HIGH_BIT, -1, -1):
				bit = (num >> k) & 1
				if bit == 0:
					if not cur.left:
						cur.left = Trie()
					cur = cur.left
				else:
					if not cur.right:
						cur.right = Trie()
					cur = cur.right

		def check(num: int) -> int:
			cur = root
			x = 0
			for k in range(HIGH_BIT, -1, -1):
				bit = (num >> k) & 1
				if bit == 0:
					if cur.right:
						cur = cur.right
						x = x * 2 + 1
					else:
						cur = cur.left
						x = x * 2
				else:
					if cur.left:
						cur = cur.left
						x = x * 2 + 1
					else:
						cur = cur.right
						x = x * 2
			return x

		n, x = len(nums), 0
		for i in range(1, n):
			add(nums[i - 1])
			x = max(x, check(nums[i]))
		return x
