class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return (n & -n) == n > 0 == (n & 0xaaaaaaaa)
