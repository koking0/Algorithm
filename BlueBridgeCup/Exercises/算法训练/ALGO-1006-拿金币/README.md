[试题 算法训练 拿金币](http://lx.lanqiao.cn/problem.page?gpid=T3000)

## Ideas

一道经典的动态规划的题目。

我们要求的是如何从最左上角走才能拿到最多的金币，并没有规定目的地，但是只能从一个格子走到它右边或下边的格子里，因此可以推出，最终肯定是在最下面一层的。

我们可以从下往上推，从最下面一层开始，逐层向上计算，得到最上面一层能够得到拿到的金币数。

## Code

### Python

```python
if __name__ == '__main__':
	n = int(input())
	dp = [[0] * (n + 1) for _ in range(n + 1)]
	for i in range(n):
		for j, val in enumerate(map(int, input().split())):
			dp[i][j] = val
	
	# 状态转移，dp[i][j] 表示在第 i 行 j 列的格子能够拿到的最多金币数，dp[i][j] = grid[i][j] + max(dp[i][j + 1], dp[i + 1][j])
	for i in range(n - 1, -1, -1):
		for j in range(n - 1, -1, -1):
			dp[i][j] = dp[i][j] + max(dp[i][j + 1], dp[i + 1][j])
	
	print(dp[0][0])
```