#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/6/5 H:37
# @File     : 面试题29. 顺时针打印矩阵.py
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
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        res, up, left, down, right = [], 0, 0, len(matrix), len(matrix[0])
        while up < down + 1 and left < right + 1:
            for i in range(left, right):
                res.append(matrix[up][i])
            up += 1
            if up > down - 1:
                break

            for i in range(up, down):
                res.append(matrix[i][right - 1])
            right -= 1
            if left > right - 1:
                break

            for i in range(right - 1, left - 1, -1):
                res.append(matrix[down - 1][i])
            down -= 1
            if up > down - 1:
                break

            for i in range(down - 1, up - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right - 1:
                break
        return res

    def spiralOrder_zip(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return res


a = Solution()
print(a.spiralOrder_zip([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
