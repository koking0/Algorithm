from collections import deque


def bfs(arr):
    n, vis, queue = len(arr), dict(), deque()
    queue.append((arr, 0))
    while queue:
        front = queue.popleft()
        tmp, cnt = front
        # print(tmp, cnt)

        if tmp == "876543210":
            print(cnt)
            return

        if vis.get(tmp, None):
            continue
        vis[tmp] = True

        idx, tmp = tmp.index("0"), list(tmp)
        for i in [-2, -1, 1, 2]:
            tmp[idx], tmp[(idx + i) % n] = tmp[(idx + i) % n], tmp[idx]
            val = ''.join(tmp)
            if not vis.get(val, None):
                queue.append((val, cnt + 1))
            tmp[idx], tmp[(idx + i) % n] = tmp[(idx + i) % n], tmp[idx]


if __name__ == '__main__':
    """
    [1, B, 3, 4, 5, 6, 7, H, 0] -> [H, 7, 6, 4, 4, 3, B, 1, 0]
    """
    sequence = "123456780"
    bfs(sequence)
