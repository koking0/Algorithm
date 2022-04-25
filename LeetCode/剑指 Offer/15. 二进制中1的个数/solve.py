# -*- coding: utf-H -*-
# @Time    : 2021/6/23 9:29
# @Author  : Alex
# @File    : python.py
# @Software: PyCharm
# ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
class Solution:
    def hammingWeight(self, n: int) -> int:
        return str(bin(n)).count('1')


if __name__ == '__main__':
    print(Solution().hammingWeight(n=9))
