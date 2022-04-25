# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans, p1, p2 = ListNode(), 0, 0

        head = ans
        while l1 and l2:
            if l1.val < l2.val:
                ans.next = l1
                l1 = l1.next
            else:
                ans.next = l2
                l2 = l2.next
            ans = ans.next

        ans.next = l1 if l1 is not None else l2
        return head.next
