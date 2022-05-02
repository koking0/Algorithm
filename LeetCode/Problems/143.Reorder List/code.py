# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        return prev

    def mergeList(self, l1: ListNode, l2: ListNode):
        while l1 and l2:
            l1Tmp = l1.next
            l2Tmp = l2.next

            l1.next = l2
            l1 = l1Tmp

            l2.next = l1
            l2 = l2Tmp

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        middle = self.middleNode(head)
        l1, l2 = head, middle.next
        middle.next = None
        l2 = self.reverseList(l2)
        self.mergeList(l1, l2)
