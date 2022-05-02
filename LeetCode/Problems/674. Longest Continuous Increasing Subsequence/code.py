class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cnt, ans = 0, 0
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0
        return ans + 1
