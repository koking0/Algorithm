import sys
from collections import deque


class BinaryTreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value, self.left, self.right = value, left, right

    @staticmethod
    def preorderTraversalRecursion(node):
        if not node:
            return
        print(node.value, end=' ')  # 递归序第一次到达 node 的时候 print
        BinaryTreeNode.preorderTraversalRecursion(node.left)
        BinaryTreeNode.preorderTraversalRecursion(node.right)

    @staticmethod
    def middleOrderTraversalRecursion(node):
        if not node:
            return
        BinaryTreeNode.middleOrderTraversalRecursion(node.left)
        print(node.value, end=' ')  # 递归序第二次达到 node 的时候 print
        BinaryTreeNode.middleOrderTraversalRecursion(node.right)

    @staticmethod
    def postorderTraversalRecursion(node):
        if not node:
            return
        BinaryTreeNode.postorderTraversalRecursion(node.left)
        BinaryTreeNode.postorderTraversalRecursion(node.right)
        print(node.value, end=' ')  # 递归序第三次达到 node 的时候 print

    @staticmethod
    def preorderTraversalLoop(node):
        if not node:
            return
        stack = [node]  # list 模拟 stack
        while stack:
            tmp = stack.pop()
            print(tmp.value, end=' ')
            if tmp.right:
                stack.append(tmp.right)
            if tmp.left:
                stack.append(tmp.left)

    @staticmethod
    def middleOrderTraversalLoop(node):
        if not node:
            return
        stack, tmp = [], node
        while stack or tmp is not None:
            if tmp:
                stack.append(tmp)
                tmp = tmp.left
            else:
                tmp = stack.pop()
                print(tmp.value, end=' ')
                tmp = tmp.right
    
    @staticmethod
    def postorderTraversalLoop(node):
        """
        preorder traversal: middle left right
        postorder traversal: left right middle
        exchange "left" and "right" then reverse print
        """
        if not node:
            return
        stack = [node]
        while stack:
            tmp = stack[-1]
            if tmp.left and node != tmp.left and node != tmp.right:
                stack.append(tmp.left)
            elif tmp.right and node != tmp.right:
                stack.append(tmp.right)
            else:
                node = tmp
                print(stack.pop().value, end=' ')

    @staticmethod
    def getMaxWidth(node):
        """ get binary tree max width """
        if not node:
            return 0

        levelMap, queue = {}, deque()
        maxWidth = curWidth = curLevel = 0
        levelMap[node] = 1
        queue.append(node)

        while queue:
            tmp = queue.popleft()
            left, right = tmp.left, tmp.right
            if left:
                levelMap[left] = levelMap[tmp] + 1
                queue.append(left)
            if right:
                levelMap[right] = levelMap[tmp] + 1
                queue.append(right)
            if levelMap[tmp] > curLevel:
                curWidth = 0
                curLevel = levelMap[tmp]
            else:
                curWidth += 1
            maxWidth = max(maxWidth, curWidth)
        return maxWidth + 1

    @staticmethod
    def isBST(node) -> bool:
        def dfs(n: BinaryTreeNode):
            if not n:
                return
            dfs(n.left)
            middleOrderList.append(n)
            dfs(n.right)

        if not head:
            return True
        middleOrderList, pre = [], -sys.maxsize
        dfs(node)

        for item in middleOrderList:
            if pre > item.value:
                return False
            pre = item.value
        return True


if __name__ == '__main__':
    head = BinaryTreeNode(1)
    head.left = BinaryTreeNode(2)
    head.right = BinaryTreeNode(3)
    head.left.left = BinaryTreeNode(4)
    head.left.right = BinaryTreeNode(5)
    head.right.left = BinaryTreeNode(6)
    head.right.right = BinaryTreeNode(7)

    print("preorder traversal (recursion):", end=' ')
    BinaryTreeNode.preorderTraversalRecursion(head)
    print()

    print("preorder traversal (loop):", end=' ')
    BinaryTreeNode.preorderTraversalLoop(head)
    print()

    print("middle order traversal (recursion):", end=' ')
    BinaryTreeNode.middleOrderTraversalRecursion(head)
    print()

    print("middle order traversal (loop):", end=' ')
    BinaryTreeNode.middleOrderTraversalLoop(head)
    print()

    print("postorder traversal (recursion):", end=' ')
    BinaryTreeNode.postorderTraversalRecursion(head)
    print()

    print("postorder traversal (loop):", end=' ')
    BinaryTreeNode.postorderTraversalLoop(head)
    print()

    print(f"max width = {BinaryTreeNode.getMaxWidth(head)}")

    print(f"is BST: {BinaryTreeNode.isBST(head)}")
