# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            nonlocal pre

            if not node:
                return
            dfs(node.left)
            node.left = None
            pre.right = node
            pre = node
            dfs(node.right)

        ans = pre = TreeNode(-1)
        dfs(root)
        return ans.right
