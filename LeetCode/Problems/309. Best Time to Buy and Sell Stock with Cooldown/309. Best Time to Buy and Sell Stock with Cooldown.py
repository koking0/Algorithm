#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/7/10 H:04
# @File     : 309. Best Time to Buy and Sell Stock with Cooldown.py
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
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        length = len(prices)
        f0, f1, f2 = -prices[0], 0, 0
        for i in range(1, length):
            nf0 = max(f0, f2 - prices[i])
            nf1 = f0 + prices[i]
            nf2 = max(f1, f2)
            f0, f1, f2 = nf0, nf1, nf2
        return max(f1, f2)
