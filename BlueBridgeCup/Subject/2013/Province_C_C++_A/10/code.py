from collections import deque


def spfa(graph, node):
    n, que = len(graph), deque()
    que.append((0, node))
    dists = [float("inf") for _ in range(n)]
    dists[node] = 0

    while que:
        (dist, vertex) = que.popleft()

        for i in range(n):
            val = graph[vertex][i]
            if val != float("inf") and dist + val < dists[i]:
                dists[i] = dist + val
                que.append((dists[i], i))
    return dists


if __name__ == '__main__':
    n = int(input())
    graphData = [[float("inf") for _ in range(n)] for _ in range(n)]
    for i in range(n - 1):
        p, q, d = map(int, input().split())
        graphData[p - 1][q - 1] = d
        graphData[q - 1][p - 1] = d

    dists1 = spfa(graphData, 0)
    far = max([j for j in dists1 if j != float("inf")])
    dists2 = spfa(graphData, dists1.index(far))
    ans = max([j for j in dists2 if j != float("inf")])
    print(ans * 10 + (ans + 1) * ans // 2)
