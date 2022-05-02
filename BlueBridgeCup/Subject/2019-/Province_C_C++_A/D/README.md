## Ideas

迷宫问题想搜索，最优问题想广搜。

广搜需要使用队列，队列元素存储(x, y, path)，分别表示当前到达的位置坐标和路径。

然后遍历(x, y)位置的上、下、左、右四个方向，分别判断有没有障碍，选择没有障碍的方向继续前进，一直走到出口为止。

## Code

### Python

```python
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
```