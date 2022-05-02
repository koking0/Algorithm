# -*- coding: utf-H -*-
# @Time    : 2021/6/21 9:03
# @Author  : Alex
# @File    : python.py
# @Software: PyCharm
# ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
from typing import List
from itertools import combinations


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        time = [1, 2, 4, 8, 1, 2, 4, 8, 16, 32]
        for item in combinations(range(len(time)), turnedOn):
            shi_list, fen_list = [], []
            for idx in item:
                if idx < 4:
                    shi_list.append(time[idx])
                else:
                    fen_list.append(time[idx])
            shi = sum(shi_list) if shi_list else 0
            fen = sum(fen_list) if fen_list else 0
            if -1 < shi < 12 and -1 < fen < 60:
                ans.append(f"{shi}:{fen:02d}")
        return ans


if __name__ == '__main__':
    print(Solution().readBinaryWatch(9))
