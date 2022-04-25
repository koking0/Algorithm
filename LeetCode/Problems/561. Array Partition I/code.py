from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans, n = 0, len(nums)
        for i in range(0, n, 2):
            ans += nums[i]
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.arrayPairSum(nums=[6, 2, 6, 5, 1, 2]))
