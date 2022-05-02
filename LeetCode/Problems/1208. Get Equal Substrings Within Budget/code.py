class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left, right, res, sums, n = 0, 0, 0, 0, len(s)
        costs = [abs(ord(s[i]) - ord(t[i])) for i in range(n)]
        while right < n:
            sums += costs[right]
            while sums > maxCost:
                sums -= costs[left]
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res
