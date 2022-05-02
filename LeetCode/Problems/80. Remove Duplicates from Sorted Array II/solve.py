from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length - 1, -1, -1):
            if i > 0 and nums[i] == nums[i - 1]:
                if i > 1 and nums[i] == nums[i - 2]:
                    del nums[i]
        return len(nums)



if __name__ == '__main__':
    print(Solution().removeDuplicates([1, 1, 1, 2, 2, 3]))
