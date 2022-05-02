from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        def findSubArray(nums):
            n = len(nums)
            zeros = res = 0
            left = right = 0
            while right < n:
                if nums[right] == 0:
                    zeros += 1
                while zeros > K:
                    if A[left] == 0:
                        zeros -= 1
                    left += 1
                res = max(res, right - left + 1)
                right += 1
            return res
        return findSubArray(A)


if __name__ == '__main__':
    s = Solution()
    print(s.longestOnes(A=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], K=2))
