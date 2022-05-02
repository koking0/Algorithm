# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def increasingBST(self, root: TreeNode) -> TreeNode:
		def middle_order_traversal(node: TreeNode):
			if node:
				stack, tmp_node, tmp_ans = [], node, ans
				while stack or tmp_node is not None:
					if tmp_node:
						stack.append(tmp_node)
						tmp_node = tmp_node.left
					else:
						tmp_node = stack.pop()
						tmp_ans.right = tmp_node
						tmp_ans = tmp_ans
						tmp_node = tmp_node.right

		ans = TreeNode()
		middle_order_traversal(root)
		return ans.right
