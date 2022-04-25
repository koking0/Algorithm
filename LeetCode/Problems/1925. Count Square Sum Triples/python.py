from math import sqrt


class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for a in range(1, n + 1):
            for b in range(a + 1, n + 1):
                c = sqrt(a ** 2 + b ** 2)
                if c % 1 == 0 and c < n + 1:
                    ans += 2
        return ans


if __name__ == '__main__':
    print(Solution().countTriples(n=5))
