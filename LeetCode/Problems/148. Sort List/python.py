from typing import Optional


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		nums = []
		node = head
		while node:
			nums.append(node.val)
			node = node.next
		nums.sort()
		node = head
		for _, v in enumerate(nums):
			node.val = v
			node = node.next
		return head
