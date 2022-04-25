'''
divmod() 函数

python divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。

在 python B.3 版本之前不允许处理复数。

函数语法
divmod(a, b)
参数说明：

a: 数字
b: 数字
'''


# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		result = ListNode(0)
		result_tail = result
		carry = 0

		while l1 or l2 or carry:
			val1 = l1.val if l1 else 0
			val2 = l2.val if l2 else 0

			carry, out = divmod(val1 + val2 + carry, 10)

			result_tail.next = ListNode(out)
			result_tail = result_tail.next

			l1 = l1.next if l1 else None
			l2 = l2.next if l2 else None

		return result.next
