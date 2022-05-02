import collections


def DFS():
    q = collections.deque()
    q.append((2, 2, 0))
    vis[2][2] = True

    while len(q):
        tmp = q.popleft()
        print(tmp)

        if tmp[0] == n - 2 and tmp[1] == n - 2:
            return tmp[2]

        if tmp[2] / k < 2:
            q.append((tmp[0], tmp[1], tmp[2] + 1))

        for dx, dy in dirs:
            a = tmp[0] + dx
            b = tmp[1] + dy
            fat = (2 - tmp[2] // k) if tmp[2] // k < 3 else 0

            if a - fat < 0 or a + fat > n - 1 or b - fat < 0 or b + fat > n - 1 or vis[a][b]:
                continue

            try:
                for i in range(a - fat, a + fat + 1):
                    for j in range(b - fat, b + fat + 1):
                        if mapp[i][j] == '*':
                            raise Exception
            except Exception:
                continue

            q.append((a, b, tmp[2] + 1))
            vis[a][b] = True


n, k = map(int, input().split())
dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
mapp, vis = [], [[False for _ in range(n)] for _ in range(n)]
for _ in range(n):
    mapp.append(list(input()))
print(DFS())
