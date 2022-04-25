# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def pre_order_traversal(node):
            if not node:
                return
            stack, ans = [node], list()
            while stack:
                tmp = stack.pop()
                if not tmp.left and not tmp.right:
                    ans.append(tmp.val)
                if tmp.right:
                    stack.append(tmp.right)
                if tmp.left:
                    stack.append(tmp.left)
            return ans
        return pre_order_traversal(root1) == pre_order_traversal(root2)
