from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index, currentDifference, miniDifference = -1, 0, max(nums)
        for i in range(len(nums) - 1):
            if nums[-1] > nums[len(nums) - 1 - i - 1]:
                currentDifference = nums[-1] - nums[len(nums) - 1 - i - 1]
                if currentDifference < miniDifference:
                    miniDifference = currentDifference
                    index = len(nums) - 1 - i - 1
        if index == -1:
            nums.sort()
        else:
            nums[index], nums[-1] = nums[-1], nums[index]


if __name__ == '__main__':
    s = Solution()
    ans = [1, 3, 2]
    s.nextPermutation(ans)
    print(ans)
