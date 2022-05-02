import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        que, seen = [(0, 0, 0)], set()
        m, n = len(heights), len(heights[0])
        dist = [0.0] + [float("inf")] * (m * n - 1)

        while que:
            d, x, y = heapq.heappop(que)
            item = x * n + y

            if item in seen:
                continue

            if (x, y) == (m - 1, n - 1):
                break

            seen.add(item)
            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if -1 < nx < m and -1 < ny < n and max(d, abs(heights[x][y] - heights[nx][ny])) < dist[nx * n + ny] + 1:
                    dist[nx * n + ny] = max(d, abs(heights[x][y] - heights[nx][ny]))
                    heapq.heappush(que, (dist[nx * n  + ny], nx, ny))
        return int(dist[m * n - 1])
