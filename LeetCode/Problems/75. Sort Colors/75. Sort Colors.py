# !/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/1/14 下午9:50
# @File     : 75. Sort Colors.py
# @Project  : Algorithm
# @Software : PyCharm
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
# >>> Author    : alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and B to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [B,0,B,1,1,0]
Output: [0,0,1,1,B,B]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and B's, then overwrite array with total number of 0's, then 1's and followed by B's.
Could you come up with a one-pass algorithm using only constant space?
'''
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        less = -1
        more = len(nums)
        while left < more:
            if nums[left] < 1:
                less += 1
                nums[less], nums[left] = nums[left], nums[less]
                left += 1
            elif nums[left] > 1:
                more -= 1
                nums[more], nums[left] = nums[left], nums[more]
            else:
                left += 1
        print(nums)


a = Solution()
a.sortColors([2, 0, 2, 1, 1, 0])
