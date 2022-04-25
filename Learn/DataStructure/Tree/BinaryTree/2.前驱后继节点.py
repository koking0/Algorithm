# 带父指针的二叉树比普通二叉树节点结构多了一个指向父节点的parent指针。
# 一棵Node类型的的二叉树，树中每个节点parent指针都指向自己的父节点，头节点的parent指向空。
# 只给一个在二叉树中的某个节点node，请实现返回node的后继节点的函数。
# 在二叉树的中序遍历的序列中，node的下一个节点叫作node的后继节点。


class Node:
    left = None
    right = None
    parent = None

    def __init__(self, value):
        self.value = value

    def in_order(self):
        if self is None:
            return
        if self.left is not None:
            self.left.in_order()
        print(self.value, end=' ')
        if self.right is not None:
            self.right.in_order()

    def next_node(self):
        """
        中序遍历的顺序是左中右，
            如果当前节点有右节点：
                当前节点一定是某一个中间节点，下一个节点是右节点所在子树的最左节点
            如果当前节点没有右节点：
                当前节点一定是某一子树的左节点，循环找到当前节点是父节点的左节点的节点，此时父节点就是后继节点
        """
        if self.right:
            temp = self.right
            while temp.left is not None:
                temp = temp.left
            return temp.value
        else:
            temp = self
            parent = self.parent
            while parent is not None and temp != parent.left:
                temp = parent
                parent = parent.parent
            return parent.value if parent else 0

    def last_node(self):
        """
        中序遍历的顺序是左中右，
            如果当前节点有左节点：
                当前节点一定是某一个中间节点，上一个节点是左节点所在子树的最右节点
            如果当前节点没有左节点：
                当前节点一定是某一子树的右节点，直接返回父节点
        """
        if self.left:
            temp = self.left
            while temp.right is not None:
                temp = temp.right
            return temp.value
        else:
            temp = self
            parent = self.parent
            while parent is not None and temp != parent.left:
                temp = parent
                parent = parent.parent
            return parent.value if parent else 0


if __name__ == '__main__':
    head = Node(1)
    head.parent = None
    head.left = Node(2)
    head.left.parent = head
    head.right = Node(3)
    head.right.parent = head
    head.left.left = Node(4)
    head.left.left.parent = head.left
    head.left.right = Node(5)
    head.left.right.parent = head.left
    head.right.left = Node(6)
    head.right.left.parent = head.right
    head.right.right = Node(7)
    head.right.right.parent = head.right

    print("in order recursive: ", end='')
    head.in_order()
    print()

    print("value = ", head.value,  " next node = ", head.next_node())
    print("value = ", head.right.value, " last node = ", head.right.last_node())
    print("value = ", head.left.right.value, " next node = ",  head.left.right.next_node())
    print("value = ", head.right.right.value, " last node = ",  head.right.right.last_node())
