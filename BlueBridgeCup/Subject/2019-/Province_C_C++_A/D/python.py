from collections import deque

if __name__ == '__main__':
	maze = []
	with open("./maze.txt") as fp:
		for line in fp.readlines():
			maze.append(list(line.strip()))
	rows, cols = len(maze), len(maze[0])
	visit = [[False] * cols for _ in range(rows)]

	queue = deque()
	queue.append((0, 0, ""))
	while queue:
		x, y, path = queue.popleft()
		if x == rows - 1 and y == cols - 1:
			print(path)
			break

		direct = ['R', 'D', 'L', 'U']
		for i, (dx, dy) in enumerate([(0, 1), (1, 0), (0, -1), (-1, 0)]):
			nx, ny = x + dx, y + dy
			if -1 < nx < rows and -1 < ny < cols and maze[nx][ny] == '0' and not visit[nx][ny]:
				queue.append((nx, ny, path + direct[i]))
				visit[nx][ny] = True
