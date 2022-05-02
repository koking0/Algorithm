# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        res = ListNode(val=0, next=head)
        cur = res
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return res.next


if __name__ == '__main__':
    h = ListNode(1)
    h.next = ListNode(2)
    h.next.next = ListNode(3)
    h.next.next.next = ListNode(3)
    h.next.next.next.next = ListNode(4)
    h.next.next.next.next.next = ListNode(4)
    h.next.next.next.next.next.next = ListNode(5)
    s = Solution()
    r = s.deleteDuplicates(head=h)
    while r:
        print(r.val)
        r = r.next

