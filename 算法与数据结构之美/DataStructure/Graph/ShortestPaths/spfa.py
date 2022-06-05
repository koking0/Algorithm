from collections import deque
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import bellman_ford


def spfa(graph, node):
    n, queue = len(graph), deque()
    queue.append((0, node))
    distance, precursor = [float("inf") for _ in range(n)], [float("inf") for _ in range(n)]
    distance[node] = 0

    while queue:
        pair = queue.popleft()
        dist, vertex = pair

        for i in range(n):
            val = graph[vertex][i]
            if val != float("inf") and dist + val < distance[i]:
                precursor[i] = vertex
                distance[i] = dist + val
                queue.append((dist + val, i))

    return distance, precursor


if __name__ == '__main__':
    graphData = [[0, 2, float("inf"), float("inf"), 10],
                 [float("inf"), 0, -3, float("inf"), 7],
                 [4, float("inf"), 0, 4, float("inf")],
                 [float("inf"), float("inf"), float("inf"), 0, 5],
                 [float("inf"), float("inf"), 3, float("inf"), 0]]

    shortest, path = spfa(graphData, 0)
    print(shortest, path)

    print('-' * 75)

    graphData = csr_matrix(graphData)
    distMatrix = bellman_ford(csgraph=graphData, directed=True, indices=0, return_predecessors=True)
    print(distMatrix)
