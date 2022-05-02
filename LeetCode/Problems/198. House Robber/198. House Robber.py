#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/5/29 6:25
# @File     : 198. House Robber.py
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
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        if length == 1:
            return nums[0]
        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, length):
            first, second = second, max(first + nums[i], second)
        return second
