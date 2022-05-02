from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack, ans = [root], []
        while stack:
            tmp = stack.pop()
            if tmp:
                ans.append(tmp.val)
                if tmp.right is not None:
                    stack.append(tmp.right)
                if tmp.left is not None:
                    stack.append(tmp.left)
        return ans


if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.right = b
    b.left = c
    s = Solution()
    ans = s.preorderTraversal(a)
    print(ans)
