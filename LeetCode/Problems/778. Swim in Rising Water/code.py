import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n, res = len(grid), 0
        visited, heap = {(0, 0)}, [(grid[0][0], 0, 0)]

        while heap:
            h, x, y = heapq.heappop(heap)
            res = max(res, h)

            if x == n - 1 and y == n - 1:
                return res

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if -1 < nx < n and -1 < ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    heapq.heappush(heap, (grid[nx][ny], nx, ny))
        return -1
