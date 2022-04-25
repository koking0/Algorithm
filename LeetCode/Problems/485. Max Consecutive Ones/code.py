from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n, left, right, ans = len(nums), 0, 0, 0
        while right < n:
            while right < n and nums[right] == 1:
                right += 1
            ans = max(ans, right - left)
            if left == right:
                left += 1
                right += 1
            else:
                left = right
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
