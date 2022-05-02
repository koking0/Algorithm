from math import sqrt


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        ans = 0
        for i in range(1, int(sqrt(num)) + 1):
            if num % i == 0:
                ans += i + (num // i if i != 1 else 0)
        return ans == num
