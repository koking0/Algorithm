from typing import List


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sumA, sumB = sum(A), sum(B)
        for i in A:
            j = (sumB + 2 * i - sumA) // 2
            if j in B:
                return [i, j]
