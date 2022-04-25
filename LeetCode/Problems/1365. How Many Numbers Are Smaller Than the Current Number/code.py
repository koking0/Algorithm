from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for item in nums:
            count = 0
            for i in range(len(nums)):
                if nums[i] < item:
                    count += 1
            ans.append(count)
        return ans


if __name__ == '__main__':
    s = Solution()
    ans = s.smallerNumbersThanCurrent([8,1,2,2,3])
    print(ans)
