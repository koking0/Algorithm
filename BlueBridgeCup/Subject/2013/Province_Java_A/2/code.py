def dfs(x, y):
	if x < 0 or y < 0 or x > 4 or y > 3:
		return 0
	if x == 4 and y == 3:
		return 1
	return dfs(x + 1, y) + dfs(x, y + 1)


if __name__ == '__main__':
	print(dfs(0, 0))
