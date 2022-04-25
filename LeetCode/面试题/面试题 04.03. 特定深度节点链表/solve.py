# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        ans = []
        level = 0
        level_map = {tree: 0}
        queue = deque()
        queue.append(tree)
        while queue:
            node = queue.popleft()
            left = node.left
            right = node.right
            if left:
                level_map[left] = level_map[node] + 1
                queue.append(left)
            if right:
                level_map[right] = level_map[node] + 1
                queue.append(right)

            if level_map[node] > level or level == 0:
                level = level_map[node]
                ans.append(ListNode(node.val))
            else:
                tmp = ans[level]
                while tmp.next:
                    tmp = tmp.next
                tmp.next = ListNode(node.val)
        return ans


if __name__ == '__main__':
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right.right = TreeNode(7)
    head.left.left.left = TreeNode(8)

    for item in Solution().listOfDepth(head):
        while item:
            print(item.val, end=" -> ")
            item = item.next
        print()
