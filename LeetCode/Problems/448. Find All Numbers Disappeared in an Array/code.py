from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if nums:
            n = len(nums)
            set1 = set([i for i in range(1, n + 1)])
            set2 = set(nums)
            return list(set1 ^ set2)
        else:
            return []


if __name__ == '__main__':
    s = Solution()
    print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
