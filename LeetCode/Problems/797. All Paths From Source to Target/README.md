[797. 所有可能的路径](https://leetcode-cn.com/problems/all-paths-from-source-to-target/)

## Ideas

首先题目要求的所有可能的路径，所以这是一个搜索问题，要搜索所有的状态空间，所以应该用DFS。

我们从0节点出发，深入探索所有可能的下一步路线，直到到达 n - 1 节点或者达到一个曾经已经访问过的节点。

## Code

### Python

```python
from typing import List
from copy import deepcopy


class Solution:
	def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
		def dfs(node, path):
			if node == n - 1:
				ans.append(deepcopy(path + [node]))
				return

			for next_node in graph[node]:
				if next_node not in path:
					path.append(node)
					dfs(next_node, path)
					path.pop()

		n = len(graph)
		ans = []
		dfs(0, [])
		return ans


if __name__ == '__main__':
	print(Solution().allPathsSourceTarget(graph=[[4, 3, 1], [3, 2, 4], [3], [4], []]))
```