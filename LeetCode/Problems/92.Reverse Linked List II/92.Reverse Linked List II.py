#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/1/29 21:37
# @File     : 92.Reverse Linked List II.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        global current_head
        if m == n:
            return head

        if m == 1:
            head_node, tail_node, help_node = self.reversed(head, n - m + 1)
            tail_node.next = help_node
            return head_node

        count = 1
        need_head = head
        while head:
            if count == m:
                head_node, tail_node, help_node = self.reversed(head, n - m + 1)
                current_head.next = head_node
                head = tail_node
                head.next = help_node
            count += 1
            current_head = head
            head = head.next
        return need_head

    def reversed(self, head: ListNode, num):
        """反转指定数目的链表，返回反转后的头节点、尾节点和下一段链表的头结点"""
        count, head_node, tail_node, help_node = 0, None, None, None
        while count < num:
            help_node = head.next
            head.next = head_node
            head_node = head
            head = help_node
            count += 1
            if tail_node is None:
                tail_node = head_node
        return head_node, tail_node, help_node


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = None
    a = Solution()
    node = a.reverseBetween(node1, 2, 4)
    while node:
        print(node.val)
        node = node.next
