# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def findFirstHalfEnd(self, node):
        fast = slow = node
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverseList(self, node):
        previous, current = None, node
        while current is not None:
            nextNode = current.next
            current.next = previous
            previous = current
            current = nextNode
        return previous

    def isPalindrome(self, head: ListNode) -> bool:
        # 判断边界情况
        if head is None:
            return True

        # 找到前半部分链表的为节点并反转后半部分链表
        firstHalfEnd = self.findFirstHalfEnd(head)
        secondHalfStart = self.reverseList(firstHalfEnd.next)

        # 判断是否为回文
        ans, firstPosition, secondPosition = True, head, secondHalfStart
        while ans and secondPosition is not None:
            if firstPosition.val != secondPosition.val:
                return False
            firstPosition = firstPosition.next
            secondPosition = secondPosition.next

        # 还原反转的链表
        firstHalfEnd.next = self.reverseList(secondHalfStart)

        return ans
