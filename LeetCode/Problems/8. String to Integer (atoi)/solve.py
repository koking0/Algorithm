import re


class Solution:
    def myAtoi(self, s: str) -> int:
        ans = re.findall('^[\+\-]?\d+', s.strip())
        return max(min(int(*ans), 2 ** 31 - 1), -2 ** 31)
