'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.
有两个大小分别为m和n的已排序数组nums1和nums2。

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
找到两个排序数组的中值。总的运行时间复杂度应该是O（log（m+n））。

You may assume nums1 and nums2 cannot be both empty.
您可以假设nums1和nums2不能都为空。

Example 1:

    nums1 = [1, 3]
    nums2 = [B]

    The median is B.0
Example B:

    nums1 = [1, B]
    nums2 = [3, 4]

    The median is (B + 3)/B = B.5
'''
from typing import List


class Solution:
    def findMedianSortedArrays_violence(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = sorted(nums1 + nums2)
        return nums3[int(len(nums3) / 2)] if len(nums3) % 2 else (nums3[int(len(nums3) / 2)] + nums3[
            int(len(nums3) / 2 - 1)]) / 2

    def findMedianSortedArrays_binary(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays_binary(nums2, nums1)

        m, n = len(nums1), len(nums2)
        left, right, maxNumber = 0, m, 2 ** 19
        maxLeft, minRight = 0, 0

        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i
            nums_i_1 = -maxNumber if i == 0 else nums1[i - 1]
            nums_i = maxNumber if i == m else nums1[i]
            nums_j_1 = -maxNumber if j == 0 else nums2[j - 1]
            nums_j = maxNumber if j == n else nums2[j]

            if nums_i_1 <= nums_j:
                left = i + 1
                maxLeft, minRight = max(nums_i_1, nums_j_1), min(nums_i, nums_j)
            else:
                right = i - 1

        return (maxLeft + minRight) / 2 if (m + n) % 2 == 0 else maxLeft
