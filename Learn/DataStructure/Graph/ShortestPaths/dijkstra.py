import heapq

from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra


def Dijkstra(graph, node):
    n, queue, visit = len(graph), list(), {node}
    heapq.heappush(queue, (0, node))
    dists, precursor = [float("inf") for _ in range(n)], [float("inf") for _ in range(n)]
    dists[node] = 0

    while queue:
        dist, vertex = heapq.heappop(queue)
        visit.add(vertex)

        for i in range(n):
            val = graph[vertex][i]
            if val != float("inf") and i not in visit and dist + val < dists[i]:
                precursor[i] = vertex
                dists[i] = dist + val
                heapq.heappush(queue, (dist + val, i))

    return dists, precursor


if __name__ == '__main__':
    graphData = [[0, 2, float("inf"), float("inf"), 10],
                 [float("inf"), 0, 3, float("inf"), 7],
                 [4, float("inf"), 0, 4, float("inf")],
                 [float("inf"), float("inf"), float("inf"), 0, 5],
                 [float("inf"), float("inf"), 3, float("inf"), 0]]

    shortest, path = Dijkstra(graphData, 0)
    print(shortest, path)

    print('-' * 75)

    graphData = csr_matrix(graphData)
    distMatrix = dijkstra(csgraph=graphData, directed=True, indices=0, return_predecessors=True)
    print(distMatrix)
