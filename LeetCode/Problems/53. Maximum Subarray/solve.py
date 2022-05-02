from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        pre = 0
        for i in nums:
            pre = max(i, pre + i)
            ans = max(ans, pre)
        return ans
