# -*- coding: utf-H -*-
# @Time    : 2021/6/23 9:33
# @Author  : Alex
# @File    : python.py
# @Software: PyCharm
# ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, pre_val = list(), float("-inf")
        while stack or root is not None:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if not root.val > pre_val:
                    return False
                pre_val = root.val
                root = root.right
        return True
