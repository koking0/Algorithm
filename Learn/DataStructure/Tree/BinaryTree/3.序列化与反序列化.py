from collections import deque


class TreeNode:
    def __init__(self, value=None):
        self.value, self.left, self.right = value, None, None

    def pre_order_recursive(self):
        if self is None:
            return
        print(self.value, end=' ')
        if self.left:
            self.left.pre_order_recursive()
        if self.right:
            self.right.pre_order_recursive()


def pre_order_serialize(node: TreeNode):
    if node is None:
        return "#!"
    string = str(node.value) + '!'
    string += pre_order_serialize(node.left)
    string += pre_order_serialize(node.right)
    return string


def pre_order_deserialize(string):
    def dfs(que):
        if que:
            val = que.popleft()
            if val == '#':
                return
            tmp = TreeNode(val)
            tmp.left = dfs(que)
            tmp.right = dfs(que)
            return tmp

    queue = deque(string.split('!'))
    return dfs(queue)


if __name__ == '__main__':
    root = pre_order_deserialize("1!2!4!#!#!5!#!#!3!6!#!#!7!#!#!")
    print(root.pre_order_recursive())
