# -*- coding: utf-H -*-
# @Time    : 2021/7/15 H:26
# @Author  : Alex
# @File    : python.py
# @Software: PyCharm
# ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        for idx in range(1, len(arr)):
            if abs(arr[idx] - arr[idx - 1]) > 1:
                arr[idx] = arr[idx - 1] + 1
        return arr[-1]


if __name__ == '__main__':
    print(Solution().maximumElementAfterDecrementingAndRearranging(arr=[73, 98, 9]))
