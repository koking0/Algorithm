import heapq
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        left = right = res = 0
        maxHeap, minHeap = [], []
        while right < n:
            heapq.heappush(minHeap, nums[right])
            heapq.heappush(maxHeap, -nums[right])
            while -heapq.nsmallest(1, maxHeap)[0] - heapq.nsmallest(1, minHeap)[0] > limit:
                if nums[left] == -heapq.nsmallest(1, maxHeap)[0]:
                    heapq.heappop(maxHeap)
                if nums[left] == heapq.nsmallest(1, minHeap)[0]:
                    heapq.heappop(minHeap)
                left += 1
            right += 1
            res = max(res, right - left)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.longestSubarray([10, 1, 2, 4, 7, 2], 5))
