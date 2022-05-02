class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return 0 < n == (n & -n)
