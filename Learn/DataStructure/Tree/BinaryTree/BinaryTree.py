import sys
from collections import deque


class BinaryTreeNode:
	def __init__(self, value=None, left=None, right=None):
		self.value, self.left, self.right = value, left, right
	
	@staticmethod
	def preTraversalRecursion(node):
		"""
		前序遍历 递归版本
		
		Args:
			node: 二叉树节点

		Returns: None
		"""
		if not node:
			return
		print(node.value, end=' ')  # 递归序第一次到达 node 的时候 print
		BinaryTreeNode.preTraversalRecursion(node.left)
		BinaryTreeNode.preTraversalRecursion(node.right)
	
	@staticmethod
	def middleTraversalRecursion(node):
		"""
		中序遍历 递归版本

		Args:
			node: 二叉树节点

		Returns: None
		"""
		if not node:
			return
		BinaryTreeNode.middleTraversalRecursion(node.left)
		print(node.value, end=' ')  # 递归序第二次达到 node 的时候 print
		BinaryTreeNode.middleTraversalRecursion(node.right)
	
	@staticmethod
	def postTraversalRecursion(node):
		"""
		后序遍历 递归版本

		Args:
			node: 二叉树节点

		Returns: None
		"""
		if not node:
			return
		BinaryTreeNode.postTraversalRecursion(node.left)
		BinaryTreeNode.postTraversalRecursion(node.right)
		print(node.value, end=' ')  # 递归序第三次达到 node 的时候 print
	
	@staticmethod
	def preTraversalLoop(node):
		"""
		前序遍历 循环版本

		Args:
			node: 二叉树节点

		Returns: None
		"""
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
	def middleTraversalLoop(node):
		"""
		中序遍历 循环版本

		Args:
			node: 二叉树节点

		Returns: None
		"""
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
	def postTraversalLoop(node):
		"""
		后序遍历 循环版本
		前序遍历顺序为：中左右，后续遍历顺序为：左右中
		所以后序遍历的即将前序遍历中“左”和“右”互换，然后整体翻转
		
		Args:
			node: 二叉树节点

		Returns: None
		"""
		stack1 = []
		if node is not None:
			stack2 = [node]
			while stack2:
				temp = stack2.pop()
				stack1.append(temp)
				if temp.left is not None:
					stack2.append(temp.left)
				if temp.right is not None:
					stack2.append(temp.right)
		while stack1:
			print(stack1.pop().value, end=' ')
	
	@staticmethod
	def postTraversalLoopPlus(node):
		"""
		后序遍历 循环优化版本 只使用 1 个栈实现
		
		Args:
			node: 二叉树节点，并且一直跟踪上一次打印的节点

		Returns: None
		"""
		if not node:
			return
		stack = [node]
		while stack:
			cur = stack[-1]
			if cur.left and node != cur.left and node != cur.right:
				# 左孩子不为空，并且 node（上次打印的节点） 既不是 cur 的左孩子也不是右孩子，即到达 1 个新的节点，开始处理左子树
				stack.append(cur.left)
			elif cur.right and node != cur.right:
				# 右孩子不为空，并且 node（上次打印的节点）不是 cur 的右孩子，即右子树还未处理，开始处理右子树
				stack.append(cur.right)
			else:  # 处理当前子树头节点
				node = cur
				print(stack.pop().value, end=' ')
	
	@staticmethod
	def levelTraversal(node):
		"""
		层序遍历
		
		Args:
			node: 二叉树节点

		Returns: None
		"""
		if not node:
			return
		queue = deque([node])
		while queue:
			cur = queue.popleft()
			print(cur.value, end=' ')
			if cur.left:
				queue.append(cur.left)
			if cur.right:
				queue.append(cur.right)
	
	@staticmethod
	def getMaxWidth(node):
		""" 层序遍历应用：二叉树最大宽度 """
		if not node:
			return 0
		
		levelMap, queue = {}, deque([node])
		maxWidth = curWidth = curLevel = 0
		levelMap[node] = 1
		
		while queue:
			tmp = queue.popleft()
			left, right = tmp.left, tmp.right
			# 层序遍历的同时记录节点所属层数
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
	def preSerialize(node):
		if node is None:
			return "#!"
		string = str(node.value) + '!'
		string += BinaryTreeNode.preSerialize(node.left)
		string += BinaryTreeNode.preSerialize(node.right)
		return string
	
	@staticmethod
	def preDeserialize(string):
		def dfs(q):
			if q:
				val = q.popleft()
				if val == '#':
					return None
				tmp = BinaryTreeNode(val)
				tmp.left = dfs(q)
				tmp.right = dfs(q)
				return tmp
		
		queue = deque(string.split('!'))
		return dfs(queue)
	
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
	
	print("pre order traversal (recursion):", end=' ')
	BinaryTreeNode.preTraversalRecursion(head)
	print()
	
	print("pre order traversal (loop):", end=' ')
	BinaryTreeNode.preTraversalLoop(head)
	print()
	
	print("middle order traversal (recursion):", end=' ')
	BinaryTreeNode.middleTraversalRecursion(head)
	print()
	
	print("middle order traversal (loop):", end=' ')
	BinaryTreeNode.middleTraversalLoop(head)
	print()
	
	print("post order traversal (recursion):", end=' ')
	BinaryTreeNode.postTraversalRecursion(head)
	print()
	
	print("post order traversal (loop):", end=' ')
	BinaryTreeNode.postTraversalLoop(head)
	print()
	
	print("level order traversal:", end=' ')
	BinaryTreeNode.levelTraversal(head)
	print()
	
	print("pre order serialize:", end=' ')
	print(BinaryTreeNode.preSerialize(head))
	
	print("pre order deserialize pre order traversal:", end=' ')
	BinaryTreeNode.preTraversalLoop(BinaryTreeNode.preDeserialize("1!2!4!#!#!5!#!#!3!6!#!#!7!#!#!"))
	print()
	
	print(f"max width = {BinaryTreeNode.getMaxWidth(head)}")
	
	print(f"is BST: {BinaryTreeNode.isBST(head)}")
