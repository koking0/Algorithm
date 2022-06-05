from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall


def FloydWarshall(graph):
    n = len(graph)
    distance = [[graph[i][j] for j in range(n)] for i in range(n)]
    precursor = [[i if graph[i][j] not in [float("inf"), 0] else float("inf") for j in range(n)] for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != j and i != k and j != k and distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    precursor[i][j] = precursor[k][j]  # i -> j 更新为 i -> k -> j，j 的前驱节点更新为原来 [k][j] 位置

    return distance, precursor


if __name__ == '__main__':
    graphData = [[0, 2, float("inf"), float("inf"), 10],
                 [float("inf"), 0, 3, float("inf"), 7],
                 [4, float("inf"), 0, 4, float("inf")],
                 [float("inf"), float("inf"), float("inf"), 0, 5],
                 [float("inf"), float("inf"), 3, float("inf"), 0]]

    shortest, path = FloydWarshall(graphData)
    for item in shortest:
        print(item)
    print()
    for item in path:
        print(item)

    print('-' * 100)

    graphData = csr_matrix(graphData)
    distMatrix, predecessors = floyd_warshall(csgraph=graphData, directed=True, return_predecessors=True)
    print(distMatrix)
    print(predecessors)
