class Node:
	def __init__(self, x, y, path):
		self.x = x
		self.y = y
		self.path = path


if __name__ == '__main__':
	matrix, queue = [], []
	with open('maze.txt') as maze:
		for item in maze.read().splitlines():
			matrix.append(list(map(int, list(item))))
	visited = [[False for _ in range(50)] for _ in range(30)]
	node = Node(0, 0, '')
	visited[0][0] = True
	queue.append(node)
	while queue:
		moveNode = queue.pop(0)
		if moveNode.x == 29 and moveNode.y == 49:
			print(moveNode.path)

		if moveNode.x < 29 and not visited[moveNode.x + 1][moveNode.y] and matrix[moveNode.x + 1][moveNode.y] == 0:
			queue.append(Node(moveNode.x + 1, moveNode.y, moveNode.path + "D"))
			visited[moveNode.x + 1][moveNode.y] = True
		if moveNode.y < 49 and not visited[moveNode.x][moveNode.y + 1] and matrix[moveNode.x][moveNode.y + 1] == 0:
			queue.append(Node(moveNode.x, moveNode.y + 1, moveNode.path + "R"))
			visited[moveNode.x][moveNode.y + 1] = True
		if moveNode.x > 0 and not visited[moveNode.x - 1][moveNode.y] and matrix[moveNode.x - 1][moveNode.y] == 0:
			queue.append(Node(moveNode.x - 1, moveNode.y, moveNode.path + "U"))
			visited[moveNode.x - 1][moveNode.y] = True
		if moveNode.y > 0 and not visited[moveNode.x][moveNode.y - 1] and matrix[moveNode.x][moveNode.y - 1] == 0:
			queue.append(Node(moveNode.x, moveNode.y - 1, moveNode.path + "L"))
			visited[moveNode.x][moveNode.y - 1] = True
