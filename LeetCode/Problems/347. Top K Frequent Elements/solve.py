from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        count = sorted(dict(count).items(), key=lambda x: x[1], reverse=True)
        return [count[i][0] for i in range(k)]


if __name__ == '__main__':
    print(Solution().topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
