#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/H/18 7:48
# @File     : code.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> WeChat    : Alex-Paddle
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def sortedListToBST(self, head: ListNode) -> TreeNode:
		def buildBST(a) -> TreeNode:
			if not a:
				return None
			return TreeNode(a[len(a) // 2], buildBST(a[:len(a) // 2]), buildBST(a[1 + len(a) // 2:]))

		array = []
		while head:
			array.append(head.val)
			head = head.next
		return buildBST(array)
