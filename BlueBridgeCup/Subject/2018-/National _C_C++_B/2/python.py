def dfs(idx):
	if idx == 30:
		global ans
		ans += 1
		return

	if light[idx - 1] == 0:
		light[idx] = 1
		dfs(idx + 1)
		light[idx] = 0
	dfs(idx + 1)


if __name__ == '__main__':
	ans, light = 0, [0] * 30
	dfs(0)
	print(ans)
