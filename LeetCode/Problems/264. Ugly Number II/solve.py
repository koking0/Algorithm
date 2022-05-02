import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        factors = [2, 3, 5]
        heap, seen = [1], {1}

        for i in range(n - 1):
            cur = heapq.heappop(heap)
            for factor in factors:
                if (item := cur * factor) not in seen:
                    seen.add(item)
                    heapq.heappush(heap, item)
        return heapq.heappop(heap)


if __name__ == '__main__':
    print(Solution().nthUglyNumber(10))
