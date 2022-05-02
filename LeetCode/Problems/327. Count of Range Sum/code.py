import bisect
from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        s = [0]
        res = cur = 0
        for v in nums:
            cur += v
            res += bisect.bisect_right(s, cur - lower) - bisect.bisect_left(s, cur - upper)
            bisect.insort_right(s, cur)
        return res
