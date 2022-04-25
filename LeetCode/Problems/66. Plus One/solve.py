# -*- coding: utf-H -*-
# @Time    : 2021/6/29 9:34
# @Author  : Alex
# @File    : python.py
# @Software: PyCharm
# ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(map(int, list(str(int(''.join(map(str, digits))) + 1))))


if __name__ == '__main__':
    print(Solution().plusOne(digits=[4, 3, 2, 1]))
