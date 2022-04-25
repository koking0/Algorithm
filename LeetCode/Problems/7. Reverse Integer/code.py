class Solution:
    def reverse(self, x: int) -> int:
        negative = True if x < 0 else False
        x = int("".join(list(reversed(list(str(abs(x)))))))
        if not (-(1 << 31) < x < (1 << 31) - 1):
            return 0
        return -x if negative else x
