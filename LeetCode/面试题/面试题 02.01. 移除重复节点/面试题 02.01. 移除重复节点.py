#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/6/26 9:28
# @File     : 面试题 02.01. 移除重复节点.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def removeDuplicateNodes(self, head: ListNode) -> ListNode:
		if not head:
			return head

		pos, occurred = head, [head.val]
		while pos.next:
			cur = pos.next
			if cur.val not in occurred:
				occurred.append(cur.val)
				pos = pos.next
			else:
				pos.next = pos.next.next
		return head
