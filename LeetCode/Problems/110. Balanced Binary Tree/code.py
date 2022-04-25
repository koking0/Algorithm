#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/H/17 H:09
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


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(node: TreeNode):
            if not node:
                return 0
            leftDepth = dfs(node.left)
            rightDepth = dfs(node.right)
            if abs(leftDepth - rightDepth) > 1:
                nonlocal flag
                flag = False
            return max(leftDepth, rightDepth) + 1

        flag = True
        dfs(root)
        return flag
