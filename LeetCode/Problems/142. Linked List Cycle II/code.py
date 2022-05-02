# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def detectCycle(self, head: ListNode) -> ListNode:
		if not head:
			return None
		slow, fast, flag = head, head, False
		while slow.next and fast.next and fast.next.next:
			slow, fast = slow.next, fast.next.next
			if slow == fast:
				flag = True
				break
		if not flag:
			return None
		slow = head
		while slow != fast:
			slow, fast = slow.next, fast.next
		return slow
