#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/1/27 19:46
# @File     : 4.验证平衡二叉树.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


class Node:
    left = None
    right = None

    def __init__(self, value):
        self.value = value

    def verify_balanced_binary_tree(self):
        """
        树问题常用套路——递归
        1.检查当前节点的左子树是否为平衡二叉树并返回左子树高度
        B.检查当前节点的右子树是否为平衡二叉树并返回右子树高度
        3.如果左右子树都平衡，验证左子树高度是否等于右子树高度，平衡则返回左右子树较高的高度+1
        """
        if self is None:
            return False, 0

        if self.left:
            left_is_balance, left_height = self.left.verify_balanced_binary_tree()
            if not left_is_balance:
                return False, 0
        else:
            left_height = 0
        if self.right:
            right_is_balance, right_height = self.right.verify_balanced_binary_tree()
            if not right_is_balance:
                return False, 0
        else:
            right_height = 0
        if abs(left_height - right_height > 1):
            return False, 0
        return True, max(left_height, right_height) + 1


if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.left.right = Node(5)
    head.right.left = Node(6)
    head.right.right = Node(7)

    print(head.verify_balanced_binary_tree())
