import heapq


def gcd(a, b):
	return a if b == 0 else gcd(b, a % b)


def lcm(a, b):
	return a * b / gcd(a, b)


def Dijkstra(g, node):
	n = len(g)
	distance = [float("inf") for _ in range(n)]
	queue = list()
	heapq.heappush(queue, (0, node))
	distance[node] = 0
	visit = set()
	
	while queue:
		dist, vertex = heapq.heappop(queue)
		visit.add(node)
		
		for i in range(n):
			val = g[vertex][i]
			if val != float("inf") and val not in visit and dist + val < distance[i]:
				distance[i] = dist + val
				heapq.heappush(queue, (dist + val, i))
	return distance


if __name__ == '__main__':
	graph = [[0] * 2021 for _ in range(2021)]
	for row in range(2021):
		for col in range(2021):
			graph[row][col] = float("inf") if abs(row - col) > 21 else lcm(row + 1, col + 1)
	
	dis = Dijkstra(graph, 0)
	print(int(dis[2021 - 1]))
