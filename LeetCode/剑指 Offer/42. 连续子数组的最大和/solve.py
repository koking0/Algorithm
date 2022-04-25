from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = curr = nums[0]
        for i in range(1, len(nums)):
            curr = nums[i] if curr < 0 < nums[i] else curr + nums[i]
            res = max(res, curr, nums[i])
        return res


if __name__ == '__main__':
    print(Solution().maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
