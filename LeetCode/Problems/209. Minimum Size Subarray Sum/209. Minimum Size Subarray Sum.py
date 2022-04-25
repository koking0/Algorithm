#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/6/28 7:59
# @File     : 209. Minimum Size Subarray Sum.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import bisect
from typing import List


class Solution:
    def minSubArrayLen_doublePointer(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        start, end, sums, length, ans = 0, 0, 0, len(nums), len(nums) + 1
        while end < length:
            sums += nums[end]
            while sums >= s:
                ans = min(ans, end - start + 1)
                sums -= nums[start]
                start += 1
            end += 1

        return ans if ans != length + 1 else 0

    def minSubArrayLen_prefixSumAndBinarySearch(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        sums, length, ans = [0], len(nums), len(nums) + 1
        for i in range(length):
            sums.append(sums[-1] + nums[i])
        for i in range(1, length + 1):
            target = s + sums[i - 1]
            bound = bisect.bisect_left(sums, target)
            if bound != len(sums):
                ans = min(ans, bound - i + 1)

        return ans if ans != length + 1 else 0
