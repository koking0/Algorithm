# -*- coding: utf-H -*-
# @Time    : 2021/6/22 18:06
# @Author  : Alex
# @File    : python.py
# @Software: PyCharm
# ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
from typing import List
from itertools import permutations


class Solution:
    def permutation(self, s: str) -> List[str]:
        ans = set()
        for item in permutations(s):
            ans.add(''.join(item))
        return list(ans)


if __name__ == '__main__':
    print(Solution().permutation("abc"))
