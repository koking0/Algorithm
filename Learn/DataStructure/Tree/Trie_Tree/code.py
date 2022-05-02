class TrieNode:
	def __init__(self, path=0, end=0):
		self.end = end
		self.path = path
		self.next_nodes = {}


class Trie:
	def __init__(self):
		self.root = TrieNode()

	@staticmethod
	def get_index(word):
		return [ord(ch) - ord('a') for ch in word]

	def insert(self, word: str) -> None:
		if not word:
			return

		node = self.root
		for idx in self.get_index(word):
			if idx not in node.next_nodes:
				node.next_nodes[idx] = TrieNode()
			node = node.next_nodes.get(idx)
			node.path += 1
		node.end += 1

	def search(self, word: str) -> bool:
		if not word:
			return False

		node = self.root
		for idx in self.get_index(word):
			if idx not in node.next_nodes:
				return False
			node = node.next_nodes.get(idx)
		return node.end != 0

	def delete(self, word: str) -> None:
		if self.search(word):
			node = self.root
			for idx in self.get_index(word):
				if node.next_node[idx].path - 1 == 0:
					node.next_node[idx].path -= 1
					node.next_node[idx] = None
					return
				node = node.next_nodes[idx]
			node.end -= 1

	def startsWith(self, prefix: str) -> bool:
		if not prefix:
			return False

		node = self.root
		for idx in self.get_index(prefix):
			if idx not in node.next_nodes:
				return False
			node = node.next_nodes[idx]
		return node.path != 0
