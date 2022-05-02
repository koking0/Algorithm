标题：迷宫

X星球的一处迷宫游乐场建在某个小山坡上，它是由10x10相互连通的小房间组成的，房间的地板上写着一个很大的字母。

我们假设玩家是面朝上坡的方向站立，则：
L表示走到左边的房间，
R表示走到右边的房间，
U表示走到上坡方向的房间，
D表示走到下坡方向的房间。

X星球的居民有点懒，不愿意费力思考，他们更喜欢玩运气类的游戏。这个游戏也是如此！

开始的时候，直升机把100名玩家放入一个个小房间内，玩家一定要按照地上的字母移动。

迷宫地图如下：
```
UDDLUULRUL
UURLLLRRRU
RRUURLDLRD
RUDDDDUUUU
URUDLLRRUU
DURLRLDLRL
ULLURLLRDU
RDLULLRDDD
UUDDUDUDLL
ULRDLUURRR
```

请你计算一下，最后，有多少玩家会走出迷宫? 而不是在里边兜圈子。

请提交该整数，表示走出迷宫的玩家数目，不要填写任何多余的内容。

如果你还没明白游戏规则，可以参看一个简化的4x4迷宫的解说图：

[](./image/p1.png)

## Ideas

首先对于迷宫问题，首先想到的就是DFS或者BFS。

这题并不是求什么最优的指标，而是想看一下有多少人能够走出迷宫，所以应该是对每一个位置都使用DFS，最终能够越界表示能够走出迷宫。

同时还有可能存在兜圈子的情况，所以需要设置一个visit数组，用来表示哪些位置已经访问过了，如果已经访问过的位置再一次被访问，则说明出现了兜圈子的情况。

## Code

### Python

```python
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
```