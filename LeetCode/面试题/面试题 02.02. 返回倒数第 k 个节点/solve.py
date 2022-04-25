# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        fast, slow = head, head
        for _ in range(k - 1):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        return slow.val


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(Solution().kthToLast(head, 2))
