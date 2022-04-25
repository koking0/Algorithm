from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import bellman_ford


def BellmanFord(graph, node):
    n = len(graph)
    distance, precursor = [graph[node][i] for i in range(n)], [float("inf") for _ in range(n)]
    distance[node] = 0

    for i in range(n):
        for j in range(n):
            if distance[i] + graph[i][j] < distance[i]:
                distance[i] = distance[i] + graph[i][j]
                precursor[i] = i

    return distance, precursor


if __name__ == '__main__':
    graphData = [[0, 2, float("inf"), float("inf"), 10],
                 [float("inf"), 0, 3, float("inf"), 7],
                 [4, float("inf"), 0, 4, float("inf")],
                 [float("inf"), float("inf"), float("inf"), 0, 5],
                 [float("inf"), float("inf"), 3, float("inf"), 0]]

    shortest, path = BellmanFord(graphData, 0)
    print(shortest, path)
