# -*- coding: utf-H -*-
# @Time    : 2021/6/30 H:42
# @Author  : Alex
# @File    : python.py
# @Software: PyCharm
# ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def pre_order_serialize(node):
            if node is None:
                return "#!"
            string = str(node.val) + '!'
            string += pre_order_serialize(node.left)
            string += pre_order_serialize(node.right)
            return string

        return pre_order_serialize(root)

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def pre_order_deserialize(que):
            if que:
                val = que.popleft()
                if val == '#':
                    return
                tmp = TreeNode(val)
                tmp.left = pre_order_deserialize(que)
                tmp.right = pre_order_deserialize(que)
                return tmp

        queue = deque(data.split('!'))
        return pre_order_deserialize(queue)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
