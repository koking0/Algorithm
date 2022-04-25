from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """ 假设首位相接，取 k 位后剩下必连续 """
        n = len(cardPoints)
        left, right = 0, n - k
        mini = sums = sum(cardPoints[left:right])
        while right < n:
            sums += cardPoints[right] - cardPoints[left]
            mini = min(sums, mini)
            left += 1
            right += 1
        return sum(cardPoints) - mini


if __name__ == '__main__':
    s = Solution()
    print(s.maxScore([96, 90, 41, 82, 39, 74, 64, 50, 30], 8))
