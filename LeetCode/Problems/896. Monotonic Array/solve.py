from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if A[0] > A[-1]:
            A.reverse()
        for i in range(1, len(A)):
            if A[i - 1] > A[i]:
                return False
        return True


if __name__ == '__main__':
    print(Solution().isMonotonic([1, 1, 0]))
