#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/H/6 H:38
# @File     : code.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> WeChat    : Alex-Paddle
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def findWord(s: str, left: int, right: int) -> int:
            return indices.get(s[left: right + 1], -1)

        def isPalindrome(s: str, left: int, right: int) -> bool:
            sub = s[left: right + 1]
            return sub == sub[::-1]

        n, ret = len(words), list()
        indices = {word[::-1]: i for i, word in enumerate(words)}

        for i, word in enumerate(words):
            m = len(word)
            for j in range(m + 1):
                if isPalindrome(word, j, m - 1):
                    leftId = findWord(word, 0, j - 1)
                    if leftId != -1 and leftId != i:
                        ret.append([i, leftId])
                if j and isPalindrome(word, 0, j - 1):
                    rightId = findWord(word, j, m - 1)
                    if rightId != -1 and rightId != i:
                        ret.append([rightId, i])
        return ret
