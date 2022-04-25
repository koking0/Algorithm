from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index, length = 0, len(nums)
        while index < length:
            if nums[index] == val:
                nums[index] = nums[length - 1]
                length -= 1
            else:
                index += 1
        return length


if __name__ == '__main__':
    print(Solution().removeElement(nums=[1], val=1))
