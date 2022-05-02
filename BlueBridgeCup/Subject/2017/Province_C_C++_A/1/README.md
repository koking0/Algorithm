���⣺�Թ�

X�����һ���Թ����ֳ�����ĳ��Сɽ���ϣ�������10x10�໥��ͨ��С������ɵģ�����ĵذ���д��һ���ܴ����ĸ��

���Ǽ���������泯���µķ���վ������
L��ʾ�ߵ���ߵķ��䣬
R��ʾ�ߵ��ұߵķ��䣬
U��ʾ�ߵ����·���ķ��䣬
D��ʾ�ߵ����·���ķ��䡣

X����ľ����е�������Ը�����˼�������Ǹ�ϲ�������������Ϸ�������ϷҲ����ˣ�

��ʼ��ʱ��ֱ������100����ҷ���һ����С�����ڣ����һ��Ҫ���յ��ϵ���ĸ�ƶ���

�Թ���ͼ���£�
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

�������һ�£�����ж�����һ��߳��Թ�? ����������߶�Ȧ�ӡ�

���ύ����������ʾ�߳��Թ��������Ŀ����Ҫ��д�κζ�������ݡ�

����㻹û������Ϸ���򣬿��Բο�һ���򻯵�4x4�Թ��Ľ�˵ͼ��

[](./image/p1.png)

## Ideas

���ȶ����Թ����⣬�����뵽�ľ���DFS����BFS��

���Ⲣ������ʲô���ŵ�ָ�꣬�����뿴һ���ж������ܹ��߳��Թ�������Ӧ���Ƕ�ÿһ��λ�ö�ʹ��DFS�������ܹ�Խ���ʾ�ܹ��߳��Թ���

ͬʱ���п��ܴ��ڶ�Ȧ�ӵ������������Ҫ����һ��visit���飬������ʾ��Щλ���Ѿ����ʹ��ˣ�����Ѿ����ʹ���λ����һ�α����ʣ���˵�������˶�Ȧ�ӵ������

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