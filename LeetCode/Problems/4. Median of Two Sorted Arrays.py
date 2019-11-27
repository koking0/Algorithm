'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.
有两个大小分别为m和n的已排序数组nums1和nums2。

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
找到两个排序数组的中值。总的运行时间复杂度应该是O（log（m+n））。

You may assume nums1 and nums2 cannot be both empty.
您可以假设nums1和nums2不能都为空。

Example 1:

    nums1 = [1, 3]
    nums2 = [2]

    The median is 2.0
Example 2:

    nums1 = [1, 2]
    nums2 = [3, 4]

    The median is (2 + 3)/2 = 2.5
'''
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = sorted(nums1 + nums2)
        return nums3[int(len(nums3) / 2)] if len(nums3) % 2 else (nums3[int(len(nums3) / 2)] + nums3[int(len(nums3) / 2 - 1)]) / 2

a = Solution()
print(a.findMedianSortedArrays([1, 2], [3, 4]))