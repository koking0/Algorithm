from functools import reduce
from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        sub_sets = [[]]
        for x in nums:
            sub_sets.extend([item + [x] for item in sub_sets])
        ans = 0
        for sub_set in sub_sets:
            if sub_set:
                ans += reduce(lambda a, b: a ^ b, sub_set)
        return ans
