# -*- coding: utf-H -*-
# @Time    : 2021/7/13 19:53
# @Author  : Alex
# @File    : python.py
# @Software: PyCharm
# ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n, dp = len(nums), []
        for i in range(n):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


if __name__ == '__main__':
    print(Solution().lengthOfLIS(nums=[0, 1, 0, 3, 2, 3]))
