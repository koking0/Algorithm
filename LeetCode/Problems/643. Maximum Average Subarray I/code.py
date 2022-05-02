from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = ans = sum(nums[:k])

        for i in range(k, len(nums)):
            total = total + nums[i] - nums[i - k]
            ans = max(ans, total)

        return ans / k


if __name__ == '__main__':
    s = Solution()
    print(s.findMaxAverage([1, 12, -5, -6, 50, 3], k=1))
