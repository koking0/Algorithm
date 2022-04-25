[1267. 统计参与通信的服务器](https://leetcode-cn.com/problems/count-servers-that-communicate/)

## Ideas

这题不想写题解了，想了半天的DFS和并查集，憋了半小时没写出来，一看题解跟我说计数。

我好难受。。。。

## Code

### Python

```python
from typing import List


class Solution:
	def countServers(self, grid: List[List[int]]) -> int:
		rows, cols, ans = len(grid), len(grid[0]), 0
		cnt_row, cnt_col = [0] * rows, [0] * cols
		for i in range(rows):
			for j in range(cols):
				if grid[i][j] == 1:
					cnt_row[i] += 1
					cnt_col[j] += 1
		for i in range(rows):
			for j in range(cols):
				if grid[i][j] == 1 and (cnt_row[i] > 1 or cnt_col[j] > 1):
					ans += 1
		return ans


if __name__ == '__main__':
	print(Solution().countServers([[1, 0], [1, 1]]))
```