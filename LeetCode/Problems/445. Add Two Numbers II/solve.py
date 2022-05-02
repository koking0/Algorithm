# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = "", ""
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        ans_num = str(int(num1) + int(num2))
        ans = ListNode(0)
        tmp = ans
        for s in ans_num:
            tmp.next = ListNode(int(s))
            tmp = tmp.next
        return ans.next
