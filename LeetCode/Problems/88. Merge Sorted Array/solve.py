from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1, idx2, tail = m - 1, n - 1, m + n - 1
        while idx1 > -1 or idx2 > -1:
            if idx1 == -1:
                nums1[tail] = nums2[idx2]
                idx2 -= 1
            elif idx2 == -1:
                nums1[tail] = nums1[idx1]
                idx1 -= 1
            elif nums1[idx1] > nums2[idx2]:
                nums1[tail] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[tail] = nums2[idx2]
                idx2 -= 1
            tail -= 1


if __name__ == '__main__':
    m, n = 3, 3
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    Solution().merge(nums1, m, nums2, n)
    print(nums1)
