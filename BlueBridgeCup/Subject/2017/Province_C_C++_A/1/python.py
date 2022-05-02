def dfs(x, y) -> bool:
	if x < 0 or x > rows - 1 or y < 0 or y > cols - 1:
		return True
	if visit[x][y]:
		return False

	visit[x][y] = True
	if maze[x][y] == 'U':
		return dfs(x - 1, y)
	if maze[x][y] == 'D':
		return dfs(x + 1, y)
	if maze[x][y] == 'L':
		return dfs(x, y - 1)
	if maze[x][y] == 'R':
		return dfs(x, y + 1)


if __name__ == '__main__':
	maze = []
	with open("maze.txt", 'r') as fp:
		for line in fp.readlines():
			maze.append(list(line.strip()))

	ans, rows, cols = 0, len(maze), len(maze[0])
	for i in range(rows):
		for j in range(cols):
			visit = [[False] * cols for _ in range(rows)]
			if dfs(i, j):
				ans += 1
	print(ans)
