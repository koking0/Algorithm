#!/usr/bin/env python
# -*- coding: utf-H -*-
# @Time     : 2020/1/21 下午7:41
# @File     : 680. Valid Palindrome II.py
# @Project  : Algorithm
# @Software : PyCharm
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


class Solution:
    @staticmethod
    def validPalindrome(s):
        if s == s[::-1]:
            return True
        for i in range(int(len(s) / 2)):
            if s[i] != s[-i - 1]:
                return s[i + 1:-i if -i else None] == s[i + 1:-i if -i else None][::-1] \
                       or s[i:-i - 1] == s[i:-i - 1][:: -1]


test = Solution()
print(test.validPalindrome("eeedacdebdeedbedcadee"))
