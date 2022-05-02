#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/6/27 H:17
# @File     : 41. First Missing Positive.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
from typing import List


class Solution:
    def firstMissingPositive_hash(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            if nums[i] <= 0:
                nums[i] = length + 1
        for i in range(length):
            num = abs(nums[i])
            if num <= length:
                nums[num - 1] = -abs(nums[num - 1])
        for i in range(length):
            if nums[i] > 0:
                return i + 1
        return length + 1

    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            while 1 <= nums[i] <= length and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(length):
            if nums[i] != i + 1:
                return i + 1
        return length + 1
