## Ideas

有点类似于线性代数的矩阵转置，不过这个是顺时针转90°，转置相当于是逆时针转90°。

但其实原理是一样的，矩阵转置是第一行变为第一列，第二行变为第二列……

顺时针转90°其实就是第一行变为第n列，第二行变为第n-1列。

## Code

### Python

```python
if __name__ == '__main__':
	n, m = map(int, input().split(' '))
	after_rotate = [[0] * n for _ in range(m)]

	for row in range(n):
		values = list(map(int, input().split(' ')))
		for col in range(m):
			after_rotate[col][n - row - 1] = values[col]

	for line in after_rotate:
		print(' '.join(map(str, line)))
```

## 在线评测：[https://www.acwing.com/problem/content/3177/](https://www.acwing.com/problem/content/3177/)