from typing import List


class Solution:
	def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
		def dfs1(u, f):
			sz[u] = 1
			dp[u] = 0
			for v in graph[u]:
				if v == f:
					continue
				dfs1(v, u)
				dp[u] += (dp[v] + sz[v])
				sz[u] += sz[v]

		def dfs2(u, f):
			ans[u] = dp[u]
			for v in graph[u]:
				if v == f:
					continue
				pu = dp[u]
				pv = dp[v]
				su = sz[u]
				sv = sz[v]
				dp[u] -= (dp[v] + sz[v])
				sz[u] -= sz[v]
				dp[v] += (dp[u] + sz[u])
				sz[v] += sz[u]
				dfs2(v, u)
				dp[u] = pu
				dp[v] = pv
				sz[u] = su
				sz[v] = sv

		sz = [0 for _ in range(N)]
		dp = [0 for _ in range(N)]
		ans = [0 for _ in range(N)]
		graph = [[] for _ in range(N)]
		for edge in edges:
			u = edge[0]
			v = edge[1]
			graph[u].append(v)
			graph[v].append(u)
		dfs1(0, -1)
		dfs2(0, -1)
		return ans
