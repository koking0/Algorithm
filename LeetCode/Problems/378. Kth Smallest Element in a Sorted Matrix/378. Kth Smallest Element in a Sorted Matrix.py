#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/B H:31
# @File     : 378. Kth Smallest Element in a Sorted Matrix.py
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
    def kthSmallest_sort(self, matrix: List[List[int]], k: int) -> int:
        rec = sorted(sum(matrix, []))
        return rec[k - 1]

    def kthSmallest_binarySearch(self, matrix: List[List[int]], k: int) -> int:
        def check(middle):
            i, j, num = length - 1, 0, 0
            while i >= 0 and j < length:
                if matrix[i][j] <= middle:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        length, left, right = len(matrix), matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
